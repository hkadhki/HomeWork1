#Задание №2

try:
    a = int(input("Введите первое число"))
    b = int(input("Введите второе число"))
    print(a/b)
except ZeroDivisionError as er1:
    print(er1)    
except ValueError as er2:
    print("Введена строка вместо числа")
    print(er2)     