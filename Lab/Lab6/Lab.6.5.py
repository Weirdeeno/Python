"""
7. Описати функцію IsPrime (N) логічного типу, яка повертає True, якщо цілий
параметр N (> 1) є простим числом, і False в іншому випадку (число, більше 1,
називається простим, якщо воно не має позитивних дільників, крім 1 і самого
себе). Дано набір з 10 цілих чисел, більших 1. За допомогою функції IsPrime
знайти кількість простих чисел в даному наборі.
"""
from math import sqrt


def IsPrime(N):
    if N < 2:
        return False
    if N == 2:
        return True
    limit = sqrt(N)
    i = 2
    while i <= limit:
        if N % i == 0:
            return False
        i += 1
    return True

count = 10
for i in range(10):
    num = int(input('Введите число > 1 : '))
    for j in range(2, int(sqrt(num)) + 1):
        if num % j == 0:
            count -= 1
            break
    print(IsPrime(num))
print('Кол-во простых чисел =',count)

