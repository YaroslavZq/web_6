--Знайти список курсів, які відвідує студент.
SELECT s.student, s2.subject
FROM marks as m
JOIN students as s ON m.student_id = s.id
JOIN subjects as s2 ON m.subject_id = s2.id
WHERE s.id = 28
GROUP BY s2.subject
ORDER BY s2.subject;