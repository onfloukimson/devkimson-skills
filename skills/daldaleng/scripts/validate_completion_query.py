#!/usr/bin/env python3
"""Validate completion SQL using in-memory synthetic students. No database connection.

Optionally --api-repo reads the actual getMmbrScheduleInfo mapper and reconciles
normal-data fixtures with modeled Java completion predicates. This is not a JVM
integration test, a SQL engine compatibility guarantee, or production validation.
"""
import argparse
import sqlite3, math, re
from datetime import date, timedelta
from pathlib import Path
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--api-repo', type=Path)
args = parser.parse_args()
sql = (Path(__file__).resolve().parents[1] / 'references/sql/completion-current.sql').read_text(encoding='utf-8')
# Dialect-only adapters; completion and report predicates are unchanged.
translated = sql.replace("CAST('2026-09-07' AS DATE)", "DATE('2026-09-07')")
translated = translated.replace("DATE_ADD(p.as_of_date, INTERVAL 1 DAY)", "DATE(p.as_of_date, '+1 DAY')")
translated = re.sub(r"INTERVAL WEEKDAY\(([^()]+)\) DAY", r"WEEKDAY(\1), 'DAY'", translated)
translated = re.sub(r"\bIF\(", "IIF(", translated)
db=sqlite3.connect(":memory:")
db.row_factory=sqlite3.Row
db.create_function("WEEKDAY",1,lambda x: date.fromisoformat(x[:10]).weekday() if x else None)
db.create_function("DATE_SUB",3,lambda x,n,u: str(date.fromisoformat(x[:10])-timedelta(days=n)) if x else None)
db.create_function("CEIL",1,lambda x: math.ceil(x) if x is not None else None)
db.executescript("""
CREATE TABLE TB_MMBR (MMBR_SEQ INTEGER PRIMARY KEY, PROFILE_NAME TEXT, MMBR_TYPE TEXT, STATUS_YN TEXT, BASIC_TEST_YN TEXT);
CREATE TABLE TB_MMBR_SCHEDULE (MMBR_SCHEDULE_SEQ INTEGER PRIMARY KEY, MMBR_SEQ INTEGER, DEL_YN TEXT, USE_YN TEXT, WEEK_CNT INTEGER, BASIC_TY TEXT, BASIC_CNT INTEGER, NOW_WEEK_NUM INTEGER, NOW_WEEK_DT TEXT);
CREATE TABLE TB_MMBR_SCHEDULE_DTL (MMBR_SCHEDULE_SEQ INTEGER, LRN_LESSON_SEQ INTEGER, SCHEDULE_ORD INTEGER, END_ROUND INTEGER, DEL_YN TEXT);
CREATE TABLE TB_LRN_LESSON (LRN_LESSON_SEQ INTEGER PRIMARY KEY, LRN_MODULE_CD TEXT, DEL_YN TEXT, USE_YN TEXT, LESSON_TY_CD TEXT);
CREATE TABLE TB_MMBR_REPORT (MMBR_SEQ INTEGER, REPORT_TY TEXT, YEAR INTEGER, MONTH INTEGER, WEEK INTEGER, REG_DT TEXT, DEL_YN TEXT, USE_YN TEXT, MMBR_SCHEDULE_SEQ INTEGER);
""")
lesson_id=0
def lesson(sid,module,ord_num,end=1,use="Y",deleted="N",typ="LTC001"):
    global lesson_id
    lesson_id+=1
    db.execute("INSERT INTO TB_LRN_LESSON VALUES (?,?,?,?,?)",(lesson_id,module,deleted,use,typ))
    db.execute("INSERT INTO TB_MMBR_SCHEDULE_DTL VALUES (?,?,?,?,?)",(sid,lesson_id,ord_num,end,"N"))
def schedule(member,sid=None,basic="Y",basic_end=1,main_end=1,now_num=2,now_date="2026-09-06",week_cnt=2,last_ord=8,use="Y"):
    sid=sid or member*100
    db.execute("INSERT INTO TB_MMBR_SCHEDULE VALUES (?,?,?,?,?,?,?,?,?)",(sid,member,"N",use,week_cnt,basic,2,now_num,now_date))
    lesson(sid,"MC002",1,basic_end)
    lesson(sid,"MC003",last_ord-1)
    lesson(sid,"MC003",last_ord,main_end,typ="LTC002")
def report(member,typ,dt="2026-09-07 04:00:00",year=2026,month=8,week=5,deleted="N",use="Y"):
    db.execute("INSERT INTO TB_MMBR_REPORT VALUES (?,?,?,?,?,?,?,?,?)",(member,typ,year,month,week,dt,deleted,use,None))
config={2:dict(main_end=0),3:dict(now_date="2026-09-07"),4:dict(now_num=1),5:dict(basic="N",basic_end=0),6:dict(basic_end=0),8:dict(now_date=None),9:dict(week_cnt=0),16:dict(last_ord=9),17:dict(last_ord=9,now_num=3),18:dict(now_date="2026-09-08"),19:dict(now_date="2026-08-30")}
for i in range(1,20):
    db.execute("INSERT INTO TB_MMBR VALUES (?,?,?,?,?)",(i,"fixture-"+str(i),"B2C","N" if i==14 else "Y","N" if i==15 else "Y"))
    schedule(i,**config.get(i,{}))
schedule(12,sid=1201,main_end=0)
schedule(13,sid=1301,main_end=0,use="N")
lesson(700,"MC003",99,0,use="N")
lesson(700,"MC003",99,0,deleted="Y")
lesson(700,"MC003",99,0,typ="LTC005")
report(1,"RT00W")
report(1,"RT00M",week=None)
report(10,"RT00W")
report(10,"RT00M",dt="2026-09-06 23:59:59")
report(11,"RT00W",week=4)
report(11,"RT00M",month=7)
report(11,"RT00M",deleted="Y")
report(11,"RT00M",use="N")
report(11,"RT00M",dt="2026-09-08 00:00:00")
rows=[dict(r) for r in db.execute(translated)]
assert [r["MMBR_SEQ"] for r in rows]==[1,5,7,10,11,13,17,19], rows
assert all(r["total_completed_students"]==8 for r in rows)
by_id={r["MMBR_SEQ"]:r for r in rows}
assert (by_id[1]["weekly_issued_today"],by_id[1]["monthly_issued_today"])==("Y","Y")
assert (by_id[10]["weekly_issued_today"],by_id[10]["monthly_issued_today"])==("Y","N")
assert (by_id[11]["weekly_issued_today"],by_id[11]["monthly_issued_today"])==("N","N")
assert by_id[7]["target_lesson_cnt"]==3 and by_id[7]["required_week_num"]==2
assert by_id[5]["target_lesson_cnt"]==2
assert by_id[17]["required_week_num"]==3
strict=translated.replace("ORDER BY m.MMBR_SEQ","AND r.weekly_report_at IS NOT NULL AND r.monthly_report_at IS NOT NULL ORDER BY m.MMBR_SEQ")
strict_rows=list(db.execute(strict))
assert len(strict_rows)==1 and strict_rows[0]["MMBR_SEQ"]==1
today=date(2026,9,7)
last_monday=today-timedelta(days=today.weekday()+7)
month_start=date(2026,8,1)
first_monday=month_start+timedelta(days=(-month_start.weekday())%7)
assert (last_monday.isoformat(),(last_monday+timedelta(days=6)).isoformat())==("2026-08-31","2026-09-06")
assert (last_monday.day-1)//7+1==5 and first_monday.isoformat()=="2026-08-03"
print("PASS: 19 synthetic students; completion, basic inclusion, active lesson types, latest schedule, Monday boundary, ceiling, report date/period/status, nullable report schedule ID, and both-report filter.")
print("PASS: August week 5 = Aug 31-Sep 6; monthly = Aug 3-Sep 6.")
print("Method: adapted SQLite fixtures. No business database connection or MariaDB execution.")

# Other read-only examples use the same fixture database and intended member scope.
query_root = Path(__file__).resolve().parents[1] / 'references/sql'
publication_sql = (query_root / 'report-publication.sql').read_text(encoding='utf-8')
publication_sql = publication_sql.replace('CAST(NULL AS SIGNED)', '1')
publication_rows = [dict(r) for r in db.execute(publication_sql)]
assert len(publication_rows) == 2
assert all(r['MMBR_SEQ'] == 1 and r['active_report_rows'] == 1 and r['rows_without_schedule_seq'] == 1 for r in publication_rows)
state_sql = (query_root / 'schedule-state.sql').read_text(encoding='utf-8')
state_sql = state_sql.replace('CAST(NULL AS SIGNED)', '1')
state_rows = [dict(r) for r in db.execute(state_sql)]
assert len(state_rows) == 1 and state_rows[0]['MMBR_SCHEDULE_SEQ'] == 100
assert state_rows[0]['completion_target_count'] == 3 and state_rows[0]['detail_unfinished_count'] == 0
print('PASS: report-publication and schedule-state examples return only the intended member and expected diagnostic counts.')


if args.api_repo:
    # Reconcile the actual mapper SELECT with the reviewed query on synthetic data.
    import xml.etree.ElementTree as ET
    mapper_path = str(args.api_repo / "src/main/resources/mapper/schedule/MmbrScheduleMapper.xml")
    element = ET.parse(mapper_path).getroot().find("./select[@id='getMmbrScheduleInfo']")
    mapper_sql = "".join(element.itertext())
    mapper_sql = re.sub(r"#\{(\w+)\}", r":\1", mapper_sql)
    mapper_sql = re.sub(r"\bIF\s*\(", "IIF(", mapper_sql, flags=re.I)
    for col in ["SCHEDULE_SEQ","SCHEDULE_VER","START_NUM","WEEK_START_DT","WEEK_START_NUM","NOW_SCHEDULE_ORD","LEVEL_ORDER","LEVEL_WRITE","REG_DT"]:
        db.execute("ALTER TABLE TB_MMBR_SCHEDULE ADD COLUMN "+col)
    db.execute("CREATE TABLE TB_MMBR_SCHEDULE_WEEK (MMBR_SEQ INTEGER,MMBR_SCHEDULE_SEQ INTEGER,YEAR INTEGER,MONTH INTEGER,WEEK INTEGER,USE_YN TEXT,MMBR_SCHEDULE_WEEK_SEQ INTEGER)")
    def week_key(d):
        monday=d-timedelta(days=d.weekday())
        jan1=date(monday.year,1,1)
        first_monday=jan1+timedelta(days=(-jan1.weekday())%7)
        return monday.year, (monday-first_monday).days//7+1
    api_completed=[]
    for member in range(1,20):
        sid=db.execute("SELECT MAX(MMBR_SCHEDULE_SEQ) FROM TB_MMBR_SCHEDULE WHERE MMBR_SEQ=? AND DEL_YN='N' AND USE_YN='Y'",(member,)).fetchone()[0]
        r=db.execute(mapper_sql,dict(mmbrSeq=member,mmbrScheduleSeq=sid,year=2026,month=9,week=1)).fetchone()
        if r["NOW_WEEK_DT"] is None or r["WEEK_CNT"] is None:
            continue
        changed=week_key(date.fromisoformat(r["NOW_WEEK_DT"]))!=week_key(today)
        all_count=(r["ALL_TOTAL_CNT"] or 0)-((r["BASIC_CNT"] or 0) if r["BASIC_TY"]=="N" else 0)
        # Java casts positive Infinity to Integer.MAX_VALUE for zero WEEK_CNT.
        required=(2147483647 if all_count>0 else (-2147483648 if all_count<0 else 0)) if r["WEEK_CNT"]==0 else math.ceil(all_count/(2.0*r["WEEK_CNT"]))
        if changed and r["ALL_LESSON_END_YN"]=="Y" and required<=r["NOW_WEEK_NUM"]:
            api_completed.append(member)
    unrestricted=translated.replace("m.STATUS_YN = 'Y' AND m.BASIC_TEST_YN = 'Y'","1=1")
    sql_completed=[r["MMBR_SEQ"] for r in db.execute(unrestricted)]
    assert api_completed==sql_completed==[1,5,7,10,11,13,14,15,17,19], (api_completed,sql_completed)
    for d in [date(2025,12,28),date(2025,12,29),date(2026,1,1),date(2026,1,4),date(2026,1,5),date(2026,8,31),date(2026,9,6),date(2026,9,7)]:
        for offset in range(-14,15):
            other=d+timedelta(days=offset)
            assert (week_key(d)==week_key(other))==((d-timedelta(days=d.weekday()))==(other-timedelta(days=other.weekday())))
    print("PASS: actual mapper SQL + modeled Java predicates match the unrestricted query for 19 fixtures; member population filters explain the two excluded fixtures.")
    print("PASS: Monday-anchor comparison matches the source week key across month/year boundary fixtures.")
