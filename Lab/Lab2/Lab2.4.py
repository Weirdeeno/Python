'''
2. Дано три цілих числа. Знайти кількість додатних чисел в початковому наборі.
'''

print("Введите три числа")
print("")
x1=int(input("Первое : "))
x2=int(input("Второе : "))
x3=int(input("Третье : "))
print("")

if x1>0 and x2>0 and x3>0:
    print("Три положительных числа")
elif x1>0 and x2>0 and x3<=0 or x1>0 and x3>0 and x2<=0 or x3>0 and x2>0 and x1<=0:
    print("Два положительных числа")
elif x1>0 and x2<=0 and x3<=0 or x1<=0 and x3>0 and x2<=0 or x3<=0 and x2>0 and x1<=0:
    print("Одно положительное число")
else:
    print("Положительных чисел нет")
