-- 코드를 입력하세요
SELECT FLAVOR
FROM FIRST_HALF as F
NATURAL JOIN ICECREAM_INFO as I
WHERE F.TOTAL_ORDER > 3000 AND I.INGREDIENT_TYPE LIKE 'fruit_based'
ORDER BY F.TOTAL_ORDER DESC;