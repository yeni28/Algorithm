
SELECT a.MEMBER_NAME , b.REVIEW_TEXT, date_format(b.REVIEW_DATE, "%Y-%m-%d") AS REVIEW_DATE
FROM MEMBER_PROFILE  a JOIN REST_REVIEW b
ON a.MEMBER_ID = b.MEMBER_ID
AND a.member_id = (SELECT b.member_id
                        FROM REST_REVIEW b
                        GROUP BY b.member_id
                        ORDER BY COUNT(*) DESC
                        LIMIT 1)
ORDER BY REVIEW_DATE, REVIEW_TEXT