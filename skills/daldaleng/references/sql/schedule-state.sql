-- Read only. This shows all active schedules for one member, not just MAX(seq).
-- It diagnoses completion inputs; it does not decide graduation.
WITH params AS (SELECT CAST(NULL AS SIGNED) AS member_seq)
SELECT s.MMBR_SEQ, s.MMBR_SCHEDULE_SEQ,
       s.BASIC_TY, s.BASIC_CNT, s.WEEK_CNT, s.NOW_WEEK_NUM, s.NOW_WEEK_DT,
       COUNT(d.LRN_LESSON_SEQ) AS detail_count,
       SUM(CASE WHEN l.LRN_LESSON_SEQ IS NOT NULL
                     AND l.USE_YN = 'Y' AND l.DEL_YN = 'N'
                     AND l.LESSON_TY_CD IN ('LTC001', 'LTC002')
                     AND (l.LRN_MODULE_CD = 'MC003'
                          OR (l.LRN_MODULE_CD = 'MC002' AND s.BASIC_TY = 'Y'))
                THEN 1 ELSE 0 END) AS completion_target_count,
       SUM(CASE WHEN d.LRN_LESSON_SEQ IS NOT NULL AND d.END_ROUND = 0
                THEN 1 ELSE 0 END) AS detail_unfinished_count,
       SUM(CASE WHEN d.LRN_LESSON_SEQ IS NOT NULL AND d.END_ROUND IS NULL
                THEN 1 ELSE 0 END) AS detail_null_end_round_count,
       SUM(CASE WHEN d.LRN_LESSON_SEQ IS NOT NULL AND l.LRN_LESSON_SEQ IS NULL
                THEN 1 ELSE 0 END) AS detail_missing_lesson_count,
       MAX(CASE WHEN l.LRN_MODULE_CD = 'MC003' AND l.USE_YN = 'Y'
                     AND l.DEL_YN = 'N' AND l.LESSON_TY_CD IN ('LTC001', 'LTC002')
                THEN d.SCHEDULE_ORD END) AS last_active_main_order
FROM TB_MMBR_SCHEDULE s
CROSS JOIN params p
LEFT JOIN TB_MMBR_SCHEDULE_DTL d
       ON d.MMBR_SCHEDULE_SEQ = s.MMBR_SCHEDULE_SEQ AND d.DEL_YN = 'N'
LEFT JOIN TB_LRN_LESSON l ON l.LRN_LESSON_SEQ = d.LRN_LESSON_SEQ
WHERE s.MMBR_SEQ = p.member_seq AND s.DEL_YN = 'N' AND s.USE_YN = 'Y'
GROUP BY s.MMBR_SEQ, s.MMBR_SCHEDULE_SEQ, s.BASIC_TY, s.BASIC_CNT,
         s.WEEK_CNT, s.NOW_WEEK_NUM, s.NOW_WEEK_DT
ORDER BY s.MMBR_SCHEDULE_SEQ DESC;
