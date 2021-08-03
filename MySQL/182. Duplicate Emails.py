# Write your MySQL query statement below

SELECT DISTINCT p.Email
FROM Person p
GROUP BY p.Email
HAVING COUNT(p.Email) > 1