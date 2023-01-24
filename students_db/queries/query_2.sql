SELECT s2.subject, ROUND(AVG(m.mark), 2) as average, s.student
FROM marks as m
JOIN students as s ON m.student_id = s.id
JOIN subjects as s2 ON m.subject_id =s2.id
WHERE s2.id = 3
--s2.id its id of subject
GROUP BY s.student, s2.subject
ORDER BY average DESC
LIMIT 1;