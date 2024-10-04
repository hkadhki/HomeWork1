#Задание №4

list = [0,1,2,3,4,5,6,7,8]

print(list)

i = int(input("Введите номер элемента списка"))

try:
    print(list[i])
except IndexError as er:
    print(er)     