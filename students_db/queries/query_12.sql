--Оцінки студентів у певній групі з певного предмета на останньому занятті.
SELECT s.subject, s2.student, m.mark, m.date_of
FROM marks as m
JOIN subjects as s ON m.subject_id = s.id
JOIN students as s2 ON m.student_id = s2.id
WHERE date_of =(SELECT MAX(date_of) from marks) AND s.id = 1 AND s2.id = 1;
