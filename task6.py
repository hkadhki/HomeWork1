#Задание №6

import math

x = int(input("Введите число:"))

try:
    sqrt = math.sqrt(x)
    print(sqrt)
except NameError as er1:
    print(er1)
except ValueError as er2:
    print("Введено отрицательное число")
    print(er2)      