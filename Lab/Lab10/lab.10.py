"""
7. Описати клас – рядок залікової книжки (екзаменаційна частина). Сформувати масив екзаменів, які
ви здали. Розробити програму, яка визначає ваш середній бал, складає список ваших екзаменаторів і
за номером семестру роздруковує результати ваших сесій.
"""

import typing


class RecordbookRecord:
    subject_name: str
    teacher: str
    date: str
    mark: int
    semester: int

    def __init__(self, subject_name, teacher, date, mark, semester):
        self.subject_name = subject_name
        self.teacher = teacher
        self.date = date
        self.mark = mark
        self.semester = semester

    def __str__(self):
        return f'{self.subject_name: <{35}} {self.teacher: <{15}} {self.date: <{12}} {self.mark: <{5}}'


exams: typing.List[RecordbookRecord] = [
    RecordbookRecord('Українська мова', 'О. Карабута', '2020-12-14', 84, 1),
    RecordbookRecord('Вікова фізіологія і валеологія', 'О. Спринь', '2020-12-15', 82, 1),
    RecordbookRecord('Групова динаміка і комунікація', 'Є. Ревенко', '2020-12-15', 90, 1),
    RecordbookRecord('Дискретна математика', 'І. Черненко', '2020-12-15', 95, 1),
    RecordbookRecord('Історія України та укр. культури', 'О. Герінбург', '2020-12-17', 84, 1),
    RecordbookRecord('Основи безпеки життэдіяльності', 'М. Фурдак', '2021-05-31', 100, 2),
    RecordbookRecord('Фізичне виховання', 'Г. Глухова', '2021-06-01', 92, 2),
    RecordbookRecord('Математичний аналіз', 'А. Бистрянцева', '2021-06-02', 74, 2),
    RecordbookRecord('Лін. алгебра та аналітична геом.', 'В. Григов’єва', '2021-06-02', 60, 2),
    RecordbookRecord('Сучасні інф. технології', 'Н. Кушнір', '2021-06-03', 100, 2),
]


def average(e: typing.List[RecordbookRecord]) -> float:
    return sum([x.mark for x in e]) / len(e)


def print_exams_by_semester(e: typing.List[RecordbookRecord], semester: int):
    e = list(filter(lambda x: x.semester == semester, e))
    for item in e:
        print(item)


a = int(input('Semester (1/2) - '))
print(f'Average: {average(exams)}')
print_exams_by_semester(exams, a)
