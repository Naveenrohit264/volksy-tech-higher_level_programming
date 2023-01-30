-- grouping
SELECT score, COUNT(*) AS number FROM second_table GROUP BY(name) ORDER BY(number) DESC;
