SELECT subject, t.teacher
FROM subjects as s
RIGHT JOIN teachers as t ON s.teacher_id = t.id
GROUP BY s.subject;