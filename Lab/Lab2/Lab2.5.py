'''
6. Дано ціле число в діапазоні 1-7. Вивести рядок - назва дня тижня, що відповідає даному числу (1 -
«понеділок», 2 - «вівторок» і т. д.)
'''

'''
Самих заданий 20 и если брать каждое 5 задание, то через четыре уже происходит повтор (7, 12, 17, 2, 7, ...)
'''

n=int(input("Введите число от 1 до 7: "))

if 1<=n<=7:
    if n==1:
        print("День недели - понедельник")
    if n==2:
        print("День недели - вторник")
    if n==3:
        print("День недели - среда")
    if n==4:
        print("День недели - четверг")
    if n==5:
        print("День недели - пятница")
    if n==6:
        print("День недели - суббота")
    if n==7:
        print("День недели - воскресенье")
else:
    print("Число введено неправильно")