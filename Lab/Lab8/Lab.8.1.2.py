"""
10. З множини чисел [1..n] виділити підмножину складних чисел виду k^2+1
"""

n = int(input('Для множества чисел [1..n] \nn : '))
s = set(range(n))


def function(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


s = filter(lambda x: not function(x), s)
s = filter(lambda x: ((x - 1) ** (1 / 2)) % 1 == 0.0, s)

print(sorted(s))
