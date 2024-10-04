#Задание №1

a = int(input("Введите первое число"))
b = int(input("Введите второе число"))

try:
    print(a/b)
except ZeroDivisionError as error:
    print(error)     