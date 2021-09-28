"""
7. Два файли з однаковою кількістю рядків. Переписати зі збереженням порядку
проходження рядки першого файлу в другий, а рядки другого файлу - в перший.
Використовувати допоміжний файл.


with open(‘f1’, ‘r’) as f1, open(‘f3’, ‘w’):
   переписать все с первого в третий

аналогично со второго в первый

аналогично с третьего во второй
"""

with open('f1.txt', 'r') as f1, open('f3.txt', 'w') as f3:
    for line in f1:
        f3.write(line)

with open('f2.txt', 'r') as f2, open('f1.txt', 'w') as f1:
    for line in f2:
        f1.write(line)

with open('f3.txt', 'r') as f3, open('f2.txt', 'w') as f2:
    for line in f3:
        f2.write(line)
