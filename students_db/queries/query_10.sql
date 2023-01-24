Список курсів, які певному студенту читає певний викладач.
SELECT s.student, t.teacher, s2.subject
FROM marks as m
JOIN students as s ON m.student_id = s.id
JOIN subjects as s2 ON m.subject_id = s2.id
JOIN teachers as t ON s2.teacher_id = t.id
WHERE s.id = 28 AND t.id = 3
GROUP BY s2.subject
ORDER BY s2.subject;