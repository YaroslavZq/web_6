SELECT ROUND(AVG(m.mark), 2), s.student
FROM marks as m
LEFT JOIN students as s ON m.student_id = s.id
GROUP BY s.student
ORDER BY ROUND(AVG(m.mark), 2) DESC
LIMIT 5;