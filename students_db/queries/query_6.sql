SELECT g.group_name, student
FROM students as s
JOIN groups as g ON s.group_id = g.id
ORDER BY g.group_name;