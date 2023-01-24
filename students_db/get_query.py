import sqlite3


def execute_query(sql: str) -> list:

	with sqlite3.connect('students.db') as con:
		cur = con.cursor()
		cur.execute(sql)
		return cur.fetchall()


# читаємо файл зі скриптом для створення БД
with open('queries/query_12.sql', 'r') as f:
	sql = f.read()


print(execute_query(sql))
