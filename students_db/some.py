from datetime import datetime
from faker import Faker
from random import randint
import sqlite3

fake = Faker('en_US')

NUMBER_GROUPS = 3
NUMBER_STUDENTS = 50  # on any group
NUMBER_TEACHERS = 5
NUMBER_SUBJECTS = 8

"""
Таблиця студентів;
Таблицю груп;
Таблицю викладачів;
Таблицю предметів із вказівкою викладача, який читає предмет;
Таблицю, де у кожного студента є оцінки з предметів із зазначенням коли оцінку отримано
"""


def generate_fake_data(number_groups: int, number_students: int, number_teachers: int, number_subjects: int) -> tuple():
    fake_groups = []  # тут зберігатимемо компанії
    fake_students = []
    fake_teachers = []  # тут зберігатимемо співробітників
    fake_subjects = []  # тут зберігатимемо посади
    '''Візьмемо три компанії з faker і помістимо їх у потрібну змінну'''

    # Створимо набір компаній у кількості number_companies
    for i in range(number_groups):
        fake_groups.append(f"Group: {str(i)}")

    # Згенеруємо тепер number_employees кількість співробітників'''
    for _ in range(number_students):
        fake_students.append(fake.name())

    for _ in range(number_teachers):
        fake_teachers.append(fake.name())

    for _ in range(number_subjects):
        fake_subjects.append(f'Subject for {fake.job()}')

    return fake_groups, fake_students, fake_teachers, fake_subjects


def prepare_data(groups: list, students: list, teachers: list, subjects: list) -> tuple():
    for_groups = []
    # підготовляємо список кортежів назв груп студентів
    for group in groups:
        for_groups.append((group, ))

    for_students = []  # для таблиці студентів

    for student in students:
        '''
        Для записів у таблицю співробітників нам треба додати посаду та id компанії. Компаній у нас було за замовчуванням
        NUMBER_COMPANIES, при створенні таблиці companies для поля id ми вказували INTEGER AUTOINCREMENT - тому кожен
        запис отримуватиме послідовне число збільшене на 1, починаючи з 1. Тому компанію вибираємо випадково
        у цьому діапазоні
        '''
        for_students.append((student, randint(1, NUMBER_GROUPS)))

    for_teachers = []
    # підготовляємо список кортежів викладачів
    for teacher in teachers:
        for_teachers.append((teacher, ))

    for_subjects = []
    # підготовляємо список кортежів назв предметів
    for subject in subjects:
        for_subjects.append((subject, randint(1, NUMBER_TEACHERS)))

    '''
    Подібні операції виконаємо й у таблиці payments виплати зарплат. Приймемо, що виплата зарплати у всіх компаніях
    виконувалася з 10 по 20 числа кожного місяця. Вилку зарплат генеруватимемо в діапазоні від 1000 до 10000 у.о.
    для кожного місяця, та кожного співробітника.
    '''
    for_marks = []

    for month in range(9, 12 + 1):
        # Виконуємо цикл по місяцях навчання загалом 4 місяці. На кожен місяць по 5 оцінок для 1 студента'''
        mark_date = datetime(2021, month, randint(10, 20)).date()
        for student in range(1, NUMBER_STUDENTS + 1):
            # Виконуємо цикл за кількістю співробітників
            for mark in range(5):
# Виконуємо цикл за 5 оцінками на місяць
                for_marks.append((randint(1, 12), mark_date, student, randint(1, NUMBER_SUBJECTS)))

    return for_groups, for_students, for_subjects, for_teachers, for_marks


def insert_data_to_db(groups: list, students: list, subjects: list, teachers: list, marks: list) -> None:
    # Створимо з'єднання з нашою БД та отримаємо об'єкт курсору для маніпуляцій з даними

    with sqlite3.connect('students.db') as con:

        cur = con.cursor()

        '''Заповнюємо таблицю компаній. І створюємо скрипт для вставки, де змінні, які вставлятимемо відзначимо
        знаком заповнювача (?) '''

        sql_to_groups = """INSERT INTO groups(group_name)
                               VALUES (?)"""

        '''Для вставки відразу всіх даних скористаємося методом executemany курсора. Першим параметром буде текст
        скрипта, а другим дані (список кортежів).'''

        cur.executemany(sql_to_groups, groups)

        # Далі вставляємо дані про співробітників. Напишемо для нього скрипт і вкажемо змінні

        sql_to_students = """INSERT INTO students(student, group_id)
                               VALUES (?, ?)"""

        # Дані були підготовлені заздалегідь, тому просто передаємо їх у функцію

        cur.executemany(sql_to_students, students)

        # Внесення даних про викладачів

        sql_to_teachers = """INSERT INTO teachers(teacher)
                              VALUES (?)"""

        cur.executemany(sql_to_teachers, teachers)

        # Внесення даних про предмети

        sql_to_subjects = """INSERT INTO subjects(subject, teacher_id)
                                      VALUES (?, ?)"""

        cur.executemany(sql_to_subjects, subjects)

        # Внесення даних про оцінки

        sql_to_marks = """INSERT INTO marks(mark, date_of, student_id, subject_id)
                                              VALUES (?, ?, ?, ?)"""

        cur.executemany(sql_to_marks, marks)

        # Фіксуємо наші зміни в БД

        con.commit()


if __name__ == "__main__":
    groups, students, subjects, teachers, marks = prepare_data(*generate_fake_data(NUMBER_GROUPS, NUMBER_STUDENTS,
                                                                                   NUMBER_TEACHERS, NUMBER_SUBJECTS))
    insert_data_to_db(groups, students, subjects, teachers, marks)
