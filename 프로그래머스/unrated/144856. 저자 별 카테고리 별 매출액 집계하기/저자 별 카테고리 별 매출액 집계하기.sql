-- 코드를 입력하세요
SELECT a.AUTHOR_ID AS AUTHOR_ID , 
b.AUTHOR_NAME AS AUTHOR_NAME , 
a.CATEGORY AS CATEGORY , 
SUM(a.PRICE * c.SALES) AS TOTAL_SALES

FROM BOOK a 

JOIN AUTHOR b 
ON a.AUTHOR_ID = b.AUTHOR_ID

JOIN BOOK_SALES c
ON a.BOOK_ID = c.BOOK_ID 

WHERE SALES_DATE LIKE "2022-01%"
GROUP BY AUTHOR_NAME , CATEGORY
ORDER BY AUTHOR_ID, CATEGORY DESC;


