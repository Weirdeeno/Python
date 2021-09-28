"""
2. Завдання: (Обробка двовимірних масивів. Кожну задачу обов’язково реалізувати за
допомогою функцій)
7. Задано список (якщо треба згенерувати відповідний список). Написати програму, яка визначає добуток
від‘ємних парних чисел першого стовпчика.
"""

from random import randint
from typing import List

n = int(input('Введіть к-ть рядків : '))
m = int(input('Введіть к-ть стовбців : '))

a = [[randint(-100, 100) for j in range(m)] for i in range(n)]
print(a)


def mas_27(list_: List[int]) -> int:
    first_column = [x[0] for x in list_]
    multiplication = 1
    for element in first_column:
        if element < 0 and element % 2 == 0:
            multiplication *= element
    return multiplication


print(mas_27(a))
