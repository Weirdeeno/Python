"""
2. Завдання: (Обробка двовимірних масивів. Кожну задачу обов’язково реалізувати за
допомогою функцій)
12. Задано список (якщо треба згенерувати відповідний список). Написати програму, яка визначає добуток
парних елементів другого стовпчика та добуток непарних елементів другого рядка матриці.
"""

from random import randint
from typing import List

n = int(input('Введіть к-ть рядків : '))
m = int(input('Введіть к-ть стовбців : '))

a = [[randint(-100, 100) for j in range(m)] for i in range(n)]
print(a)


def mas_212(list_: List[int]) -> int:
    second_column = [x[1] for x in list_]
    multiplication = 1
    for element_1 in second_column:
        if element_1 > 0 and element_1 % 2 == 0:
            multiplication *= element_1
    return multiplication


def mas_212_2(list_: List[int]) -> int:
    multiplication = 1
    second_row = list_[1]
    for element_2 in second_row:
        if element_2 % 2:
            multiplication *= element_2
    return multiplication


print(mas_212(a))
print(mas_212_2(a))