-- Read only. Replace NULL with the intended internal MMBR_SEQ.
-- Example report period: August week 5, 2026. No issue-date restriction.
WITH params AS (
    SELECT CAST(NULL AS SIGNED) AS member_seq,
           2026 AS report_year, 8 AS report_month, 5 AS report_week
)
SELECT r.MMBR_SEQ, r.REPORT_TY, r.YEAR, r.MONTH, r.WEEK,
       COUNT(*) AS active_report_rows,
       MIN(r.REG_DT) AS first_active_created_at,
       MAX(r.REG_DT) AS last_active_created_at,
       SUM(CASE WHEN r.MMBR_SCHEDULE_SEQ IS NULL THEN 1 ELSE 0 END)
           AS rows_without_schedule_seq
FROM TB_MMBR_REPORT r
CROSS JOIN params p
WHERE r.MMBR_SEQ = p.member_seq
  AND r.DEL_YN = 'N' AND r.USE_YN = 'Y'
  AND r.YEAR = p.report_year AND r.MONTH = p.report_month
  AND ((r.REPORT_TY = 'RT00W' AND r.WEEK = p.report_week)
       OR r.REPORT_TY = 'RT00M')
GROUP BY r.MMBR_SEQ, r.REPORT_TY, r.YEAR, r.MONTH, r.WEEK
ORDER BY r.REPORT_TY, r.WEEK;
