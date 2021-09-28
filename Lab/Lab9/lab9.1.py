"""
Завдання 1.
Створіть файли, у яких будуть міститися рядки з іменами студентів та їх середніми балами.
Реалізуйте читання файлів, запис та дозапис у файли, пошук файлів у каталозі та пошук
даних у файлі. Також реалізуйте сортування даних у файлі за середнім балом.
"""

import os


def operation_number(x):
    return x == '1' or x == '2' or x == '3' or x == '4' or x == '5' or x == '6'


n = None
while not operation_number(n):
    print('Операції:\n'
          'Читання файлів - 1\n'
          'Запис у файли - 2\n'
          'Дозапис у файли - 3\n'
          'Пошук файла у каталозі - 4\n'
          'Пошук даних у файлі - 5\n'
          'Сортування даних за середнім бaлом - 6\n'
          'Вихід - 0'
          )
    n = int(input('\nВведіть номер операції: '))

    if n == 1:
        print('1. Прочитати всі файли\n'
              'Прочитати певний файл:\n'
              '2.1 111.txt\n'
              '2.2 131.txt\n'
              '2.3 132.txt\n'
              '2.4 161.txt\n'
              '2.5 141.txt\n')
        n1 = input('Введіть номер операції: ')
        if n1 == '1':
            with open("111.txt", "r", encoding='utf-8') as file_1, open("131.txt", "r",encoding='utf-8') as file_2, open('132.txt','r',encoding='utf-8') as file_3, open('161.txt', "r", encoding='utf-8') as file_4, open('141.txt', "r", encoding='utf-8') as file_5:
                text = file_1.read() + file_2.read() + file_3.read() + file_4.read() + file_5.read()
                print(text)
        elif n1 == '2.1':
            with open('111.txt', 'r', encoding='utf-8') as f:
                text = f.read()
                print(text)
        elif n1 == '2.2':
            with open('131.txt', 'r', encoding='utf-8') as f:
                text = f.read()
                print(text)
        elif n1 == '2.3':
            with open('132.txt', 'r', encoding='utf-8') as f:
                text = f.read()
                print(text)
        elif n1 == '2.4':
            with open('161.txt', 'r', encoding='utf-8') as f:
                text = f.read()
                print(text)
        elif n1 == '2.5':
            with open('141.txt', 'r', encoding='utf-8') as f:
                text = f.read()
                print(text)

    elif n == 2:
        print(
              '1. 111.txt\n'
              '2. 131.txt\n'
              '3. 132.txt\n'
              '4. 161.txt\n'
              '5. 141.txt\n')
        name = input('Виберіть файл для запису: ')
        if name == '1':
            with open('111.txt', 'w', encoding='utf-8') as file:
                line = input('Введіть текст: ')
                file.writelines(line)
        if name == '2':
            with open('131.txt', 'w', encoding='utf-8') as file:
                line = input('Введіть текст: ')
                file.writelines(line)
        if name == '3':
            with open('132.txt', 'w', encoding='utf-8') as file:
                line = input('Введіть текст: ')
                file.writelines(line)
        if name == '4':
            with open('161.txt', 'w', encoding='utf-8') as file:
                line = input('Введіть текст: ')
                file.writelines(line)
        if name == '5':
            with open('141.txt', 'w', encoding='utf-8') as file:
                line = input('Введіть текст: ')
                file.writelines(line)

    elif n == 3:
        print(
            '1. 111.txt\n'
            '2. 131.txt\n'
            '3. 132.txt\n'
            '4. 161.txt\n'
            '5. 141.txt\n')
        name = input('Виберіть файл для дозапису: ')
        if name == '1':
            with open('111.txt', 'a', encoding='utf-8') as file:
                line = input('Введіть текст: ')
                file.writelines('\n' + line)
        if name == '2':
            with open('131.txt', 'a', encoding='utf-8') as file:
                line = input('Введіть текст: ')
                file.writelines('\n' + line)
        if name == '3':
            with open('132.txt', 'a', encoding='utf-8') as file:
                line = input('Введіть текст: ')
                file.writelines('\n' + line)
        if name == '4':
            with open('161.txt', 'a', encoding='utf-8') as file:
                line = input('Введіть текст: ')
                file.writelines('\n' + line)
        if name == '5':
            with open('141.txt', 'a', encoding='utf-8') as file:
                line = input('Введіть текст: ')
                file.writelines('\n' + line)

    elif n == 4:
        name = input('Введіть назву файлу (назва.txt): ')
        if name in os.listdir():
            print('Файл є в каталозі')
        else:
            print('Файлу немає в каталозі')

    elif n == 5:
        print(
              '1. 111.txt\n'
              '2. 131.txt\n'
              '3. 132.txt\n'
              '4. 161.txt\n'
              '5. 141.txt\n')
        name = input('Виберіть файл для пошуку: ')
        if name == '1':
            with open('111.txt', encoding='utf-8') as file:
                text = input('Введіть початок шуканого ряда: ')
                for line in file:
                    line = line.rstrip()
                    if line.startswith(text):
                        print(line)
        elif name == '2':
            with open('131.txt', encoding='utf-8') as file:
                text = input('Введіть початок шуканого ряда: ')
                for line in file:
                    line = line.rstrip()
                    if line.startswith(text):
                        print(line)
        elif name == '3':
            with open('132.txt', encoding='utf-8') as file:
                text = input('Введіть початок шуканого ряда: ')
                for line in file:
                    line = line.rstrip()
                    if line.startswith(text):
                        print(line)
        elif name == '4':
            with open('161.txt', encoding='utf-8') as file:
                text = input('Введіть початок шуканого ряда: ')
                for line in file:
                    line = line.rstrip()
                    if line.startswith(text):
                        print(line)
        elif name == '5':
            with open('141.txt', encoding='utf-8') as file:
                text = input('Введіть початок шуканого ряда: ')
                for line in file:
                    line = line.rstrip()
                    if line.startswith(text):
                        print(line)

    elif n == 6:
        print(
              '1. 111.txt\n'
              '2. 131.txt\n'
              '3. 132.txt\n'
              '4. 161.txt\n'
              '5. 141.txt\n')
        name = input('Введіть назву файлу (назва.txt) для сортування: ')
        lines = open(name, 'r').readlines()
        output = open(name, 'w')

        for line in sorted(lines, key=lambda line: line.split()[1]):
            output.write(line)

        output.close()
        with open(name, 'r', encoding='utf-8') as f:
            text = f.read()
            print(text)

    elif n == 0:
        break
