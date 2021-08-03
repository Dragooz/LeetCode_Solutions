# Write your MySQL query statement below

SELECT S.Score, COUNT(S2.Score) AS `Rank`
FROM Scores as S, (SELECT DISTINCT Score from Scores) as S2
WHERE S2.Score >= S.Score
GROUP BY S.Id
ORDER BY `Rank`