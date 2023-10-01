SELECT a.FOOD_TYPE, a.REST_ID, a.REST_NAME, a.FAVORITES
FROM rest_info a
JOIN (SELECT food_type, max(favorites) AS max_fav
FROM rest_info  
GROUP BY food_type) b
ON a.food_type = b.food_type
AND a.favorites = b.max_fav 
ORDER BY food_type desc