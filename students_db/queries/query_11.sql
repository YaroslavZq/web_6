--Середній бал, який певний викладач ставить певному студентові.
SELECT t.teacher, s2.student, ROUND(AVG(m.mark), 2) as average
FROM marks as m
JOIN subjects as s ON m.subject_id = s.id
JOIN teachers as t ON s.teacher_id = t.id
JOIN students as s2 ON m.student_id = s2.id
WHERE t.id = 3 AND s2.id = 3;