import random
import re
import itertools

# 1.Введення списку
print('1.Введення списку')
i_list = input("Введіть потрібні елементи в список через пробіл: ").split(' ')
print('')

# 2.Заповнення списку випадковими числами
print('2.Заповнення списку випадковими числами')
size = int(input('Введіть кількість випадкових елементів: '))
r_list = [random.randint(-100, 100) for _ in range(0, size)]
print('')


# 3.Виведення списку
def output_list_1():
    """
    :return: outputting an introductory list (i_list)
    """
    print(i_list)


def output_list_2():
    """
    :return outputting a list with random numbers (r_list)
    """
    print(r_list)


# 4.Пошук елемента за значенням
def search_item_1(need_element):
    """
    :param need_element: element introduction
    If the item is in the i_list :
    :return:'Даний елемент є в списку!'
    If the item is not in the i_list :
    :return:'Такого елемента в списку не знайдено!'
    """
    need_element = input('Введіть елемент який бажаєте знайти: ')
    if i_list.count(need_element):
        return 'Даний елемент є в списку!'
    else:
        return 'Такого елемента в списку не знайдено!'


def search_item_2(need_element):
    """
   :param need_element: element introduction
    If the item is in the r_list :
    :return:'Даний елемент є в списку!'
    If the item is not in the r_list :
    :return:'Такого елемента в списку не знайдено!'
    """
    need_element = int(input('Введіть елемент який бажаєте знайти: '))
    if r_list.count(need_element):
        return 'Даний елемент є в списку!'
    else:
        return 'Такого елемента в списку не знайдено!'


# 5.Пошук максимального елемента
def search_max_1():
    """
    :return: finds the maximum value in the list
    """
    return max(i_list)


def search_max_2():
    """
    :return: finds the maximum value in the list (r_list)
    """
    return max(r_list)


# 6.Сортування списку за зростанням (спаданням)
def sorting_list_1(choice):
    """
    :param choice: input value which is 1 or 2
    If choice is 1
    :return: descending sorted i_list
    If choice is 2
    :return: ascending sorted i_list
    """
    choice = input('Виберіть сортування (1 - за спаданням, 2 - за зростанням) : ')
    if choice == '1':
        return sorted(i_list, reverse=True)
    elif choice == '2':
        return sorted(i_list)


def sorting_list_2(choice):
    """
    :param choice: input value which is 1 or 2
    If choice is 1
    :return: descending sorted r_list
    If choice is 2
    :return: ascending sorted r_list
    """
    choice = input('Виберіть сортування (1 - за спаданням, 2 - за зростанням) : ')
    if choice == '1':
        return sorted(r_list, reverse=True)
    elif choice == '2':
        return sorted(r_list)


# 7.Пошук середнього арифметичного
def search_average_1():
    """
    :return: finds the arithmetic mean of a list (i_list)
    """
    return float(sum([float(x) for x in i_list]) / max(len(i_list), 1))


def search_average_2():
    """
    :return: finds the arithmetic mean of a list (r_list)
    """
    return float(sum(r_list) / max(len(r_list), 1))
