with a as(
    SELECT CAR_ID
    from CAR_RENTAL_COMPANY_RENTAL_HISTORY 
    where date_format(START_DATE, '%Y-%m') between '2022-08' and '2022-10'
    group by CAR_ID
    having count(*) >= 5
)

SELECT date_format(START_DATE, '%m') as MONTH, CAR_ID, count(*) as RECORDS
from CAR_RENTAL_COMPANY_RENTAL_HISTORY 
where (date_format(START_DATE, '%Y-%m') between '2022-08' and '2022-10') 
    and CAR_ID in (select * from a)
group by MONTH, CAR_ID
order by MONTH, CAR_ID desc