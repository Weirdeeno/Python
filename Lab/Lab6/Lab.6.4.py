"""
7. Описати функцію Ln1 (x, ε) дійсного типу (параметри x, ε - дійсні, | x | <1, ε> 0),
знаходить наближене значення функції ln (1 + x):
ln (1 + x) = x - x^2 / 2 + x^3 / 3 - ... + (-1)^n · x^(n + 1) / (n + 1) + ....
В сумі враховувати всі складові, модуль яких більше ε. За допомогою Ln1
знайти наближене значення ln (1 + x) для даного x при шести даних ε.
"""

from math import *

n = float(input("Введите число n - "))
x = float(input("Введите x, |x| < 1 - "))
print()
eps = [0.00001, 0.0001, 0.001, 0.01, 0.1, 1]


def ln(x, n, eps):
    res = 0
    while n + 1:
        elem = (pow(-1, n) * pow(x, (n + 1))) / (n + 1)
        if abs(elem) > eps:
            res += elem
        n -= 1
    return res


for i in range(0, 6):
    print("ln(x+1) = ", ln(x, n, eps[i]), ", при n = " + str(n) + ", x = " + str(x) + ", eps = " + str(eps[i]))
