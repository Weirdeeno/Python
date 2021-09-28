'''
3. Дано два ненульових числа. Знайти суму, різницю, добуток і частку їх квадратів
'''

a=int(input("Введите число a - "))
b=int(input("Введите число b - "))

S = a**2 + b**2
R1 = a**2 - b**2
R2 = b**2 - a**2
D = a**2 * b**2
Ch1 = a**2 / b**2
Ch2 = b**2 / a**2

print("")
print("a^2 + b^2 =", S)
print("")
print("a^2 - b^2 =", R1)
print("b^2 - a^2 =", R2)
print("")
print("a^2 * b^2 =", D)
print("")
print("a^2 / b^2 =", Ch1)
print("b^2 / a^2 =", Ch2)
print("")