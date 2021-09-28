"""
9. Описати рекурсивну функцію Palindrome (S) логічного типу, яка повертає True,
якщо ціле S є паліндромом (Читається однаково зліва направо і справа наліво),
і False в іншому випадку. Оператор циклу в тілі функції не використовувати.
Вивести значення функції Palindrome для п'яти даних чисел.
"""
def Palindrom(S):
    if len(S) >= 2:
        return (S[0] == S[-1:-2:-1]) and Palindrom(S[1:-1])
    return True

for i in range(0,5):
    s = input('Введите число : ')
    t = s.replace(" ", "").lower()
    print("Palindrom:",Palindrom(t))