/*
목적 :
아웃풋 : PRICE_GROUP, PRODUCTS
조건
1.구간의 최소금액(10,000원 이상 ~ 20,000 미만인 구간인 경우 10,000)으로 표시
2.결과는 가격대를 기준
*/

SELECT
    CASE 
        WHEN price >= 10000 AND price < 20000 THEN 10000
        WHEN price >= 20000 AND price < 30000 THEN 20000
        WHEN price >= 30000 AND price < 40000 THEN 30000
        WHEN price >= 40000 AND price < 50000 THEN 40000
        WHEN price >= 50000 AND price < 60000 THEN 50000
        WHEN price >= 60000 AND price < 70000 THEN 60000
        WHEN price >= 70000 AND price < 80000 THEN 70000
        WHEN price >= 80000 AND price < 90000 THEN 80000
        END AS PRICE_GROUP
    ,COUNT(product_id) AS PRODUCTS
FROM PRODUCT
GROUP BY 1
ORDER BY 1