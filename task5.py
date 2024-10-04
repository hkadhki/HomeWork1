#Задание №5

string = input("Введите число с плавающей точкой")

try:
    x = float(string)
    print(x)
except ValueError as er:
    print(er)     