'''
15. Дано змінні A, B, C. Змінити їх значення, перемістивши вміст A в B, B - в C, C - в A, і вивести
нові значення змінних A, B, C.
'''

A = int(input("Введите А - "))
B = int(input("Введите В - "))
C = int(input("Введите С - "))

A,B,C=C,A,B

print(A,B,C)