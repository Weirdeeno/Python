'''
7. Дано ціле число N (> 2) і дві дійсні точки на числовій осі: A, B (A <B). Функція F (X) задана
формулою F (X) = 1 - sin (X). Вивести значення функції F в N рівновіддалених точках, що
утворюють розбиття відрізка [A, B]: F (A), F (A + H), F (A + 2H), ..., F (B).
'''

import math
n=int(input("Введите N > 2 : "))
a=float(input("Введите начало отрезка A : "))
b=float(input("Введите конец отрезка B : "))
n += 1
h=(b-a)/n
func = lambda x:1-math.sin(x)

current = a + h
while current < (b - h / 2):
    print("Точка =", current, "Значение функции =", func(current))
    current += h
    
 