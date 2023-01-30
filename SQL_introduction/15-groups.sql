-- grouping
SELECT score, COUNT(*) as number FROM second_table GROUP BY name, ORDER BY number DESC;
