--Знайти оцінки студентів у окремій групі з певного предмета.
SELECT s2.subject, g.group_name, s.student, m.mark
FROM marks as m
JOIN students as s ON m.student_id = s.id
JOIN groups as g ON s.group_id = g.id
JOIN subjects as s2 ON m.subject_id = s2.id
WHERE m.subject_id = 3
ORDER BY s.student