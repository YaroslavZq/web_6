--Знайти середній бал, який ставить певний викладач зі своїх предметів.
SELECT t.teacher, ROUND(AVG(m.mark), 2) as average
FROM marks as m
JOIN subjects as s ON m.subject_id = s.id
JOIN teachers as t ON s.teacher_id = t.id
WHERE t.id = 2;