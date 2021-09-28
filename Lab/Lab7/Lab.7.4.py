"""
7. Описати рекурсивну функцію GCD (A, B) цілого типу, яка знаходить найбільший
спільний дільник (НСД, greatest common divisor) двох цілих позитивних чисел A і
B, використовуючи алгоритм Евкліда:
НСД (A, B) = НСД (B, A mod B), B ≠ 0; НСД (A, 0) = A,
де «mod» позначає операцію взяття залишку від ділення. За допомогою цієї
функції знайти НСД (A, B), НCД (A, C), НCД (A, D), якщо дано числа A, B, C, D.
"""


def GCD(A, B):
    if B != 0:
        return GCD(B, A % B)
    else:
        return A


A = int(input("A = "))
B = int(input("B = "))
C = int(input("C = "))
D = int(input("D = "))

print("НСД({0},{1}) = {2}".format(A, B, GCD(A, B)))
print("НСД({0},{1}) = {2}".format(A, C, GCD(A, C)))
print("НСД({0},{1}) = {2}".format(A, D, GCD(A, D)))