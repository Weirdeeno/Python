'''
2. Дано рядок, що містить повне ім'я файлу (наприклад, C:\WebServers\home\testsite\www\myfile.txt').
Виділіть з цього рядка ім'я файлу без розширення.
'''

from os import path
full_name = path.basename('C:\WebServers\home\testsite\www\myfile.txt')
name = path.splitext(full_name)[0]
print('Имя файла без расширения -',name)