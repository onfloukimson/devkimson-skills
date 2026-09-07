-- 기준일: 2026-09-07 (KST), 대상: 2026년 8월 5주차 / 8월 월간
WITH
params AS (
    SELECT CAST('2026-09-07' AS DATE) AS as_of_date,
           2026 AS report_year, 8 AS report_month, 5 AS report_week
),
latest_schedule AS (
    SELECT s.*
    FROM TB_MMBR_SCHEDULE s
    JOIN (
        SELECT MMBR_SEQ, MAX(MMBR_SCHEDULE_SEQ) AS schedule_seq
        FROM TB_MMBR_SCHEDULE
        WHERE DEL_YN = 'N' AND USE_YN = 'Y'
        GROUP BY MMBR_SEQ
    ) x ON x.schedule_seq = s.MMBR_SCHEDULE_SEQ
),
lesson_summary AS (
    SELECT s.MMBR_SCHEDULE_SEQ,
           COUNT(l.LRN_LESSON_SEQ) AS target_lesson_cnt,
           SUM(CASE WHEN l.LRN_LESSON_SEQ IS NOT NULL
                         AND d.END_ROUND = 0 THEN 1 ELSE 0 END) AS unfinished_cnt,
           COALESCE(MAX(CASE WHEN l.LRN_MODULE_CD = 'MC003'
                             THEN d.SCHEDULE_ORD END), 0) AS last_main_ord
    FROM latest_schedule s
    LEFT JOIN TB_MMBR_SCHEDULE_DTL d
           ON d.MMBR_SCHEDULE_SEQ = s.MMBR_SCHEDULE_SEQ
          AND d.DEL_YN = 'N'
    LEFT JOIN TB_LRN_LESSON l
           ON l.LRN_LESSON_SEQ = d.LRN_LESSON_SEQ
          AND l.DEL_YN = 'N' AND l.USE_YN = 'Y'
          AND l.LESSON_TY_CD IN ('LTC001', 'LTC002')
          AND (l.LRN_MODULE_CD = 'MC003'
               OR (l.LRN_MODULE_CD = 'MC002' AND s.BASIC_TY = 'Y'))
    GROUP BY s.MMBR_SCHEDULE_SEQ
),
completion AS (
    SELECT s.*, ls.target_lesson_cnt, ls.unfinished_cnt,
           CEIL(
               (ls.last_main_ord
                - CASE WHEN s.BASIC_TY = 'N'
                       THEN COALESCE(s.BASIC_CNT, 0) ELSE 0 END)
               / (2.0 * NULLIF(s.WEEK_CNT, 0))
           ) AS required_week_num
    FROM latest_schedule s
    JOIN lesson_summary ls
      ON ls.MMBR_SCHEDULE_SEQ = s.MMBR_SCHEDULE_SEQ
),
issued_reports AS (
    SELECT r.MMBR_SEQ,
           MAX(CASE WHEN r.REPORT_TY = 'RT00W' THEN r.REG_DT END) AS weekly_report_at,
           MAX(CASE WHEN r.REPORT_TY = 'RT00M' THEN r.REG_DT END) AS monthly_report_at
    FROM TB_MMBR_REPORT r
    CROSS JOIN params p
    WHERE r.DEL_YN = 'N' AND r.USE_YN = 'Y'
      AND r.YEAR = p.report_year AND r.MONTH = p.report_month
      AND ((r.REPORT_TY = 'RT00W' AND r.WEEK = p.report_week)
            OR r.REPORT_TY = 'RT00M')
      AND r.REG_DT >= p.as_of_date
      AND r.REG_DT < DATE_ADD(p.as_of_date, INTERVAL 1 DAY)
    GROUP BY r.MMBR_SEQ
)
SELECT COUNT(*) OVER () AS total_completed_students,
       m.MMBR_SEQ, m.MMBR_TYPE,
       c.MMBR_SCHEDULE_SEQ,
       c.target_lesson_cnt, c.unfinished_cnt,
       c.NOW_WEEK_NUM, c.required_week_num, c.NOW_WEEK_DT,
       IF(r.weekly_report_at IS NOT NULL, 'Y', 'N') AS weekly_issued_today,
       IF(r.monthly_report_at IS NOT NULL, 'Y', 'N') AS monthly_issued_today,
       r.weekly_report_at, r.monthly_report_at
FROM completion c
JOIN TB_MMBR m ON m.MMBR_SEQ = c.MMBR_SEQ
CROSS JOIN params p
LEFT JOIN issued_reports r ON r.MMBR_SEQ = c.MMBR_SEQ
WHERE m.STATUS_YN = 'Y' AND m.BASIC_TEST_YN = 'Y'
  AND c.WEEK_CNT > 0
  AND c.unfinished_cnt = 0
  AND c.NOW_WEEK_NUM >= c.required_week_num
  AND c.NOW_WEEK_DT IS NOT NULL
  AND DATE_SUB(DATE(c.NOW_WEEK_DT), INTERVAL WEEKDAY(c.NOW_WEEK_DT) DAY)
      <> DATE_SUB(p.as_of_date, INTERVAL WEEKDAY(p.as_of_date) DAY)
-- 오늘 두 리포트가 모두 발행된 완강 학생만 보려면 아래 두 줄의 주석 해제
--  AND r.weekly_report_at IS NOT NULL
--  AND r.monthly_report_at IS NOT NULL
ORDER BY m.MMBR_SEQ;
