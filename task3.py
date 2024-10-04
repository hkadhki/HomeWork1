#Задание №3

class EvenException (Exception):
    pass

class NegativeException (Exception):
    pass


def test_even(list):
    for i in list:
        if i % 2 == 0:
            raise EvenException("В списке есть четные числа")
        
def test_negative(list):
    for i in list:
        if i < 0:
            raise NegativeException("В списке есть отрицательные числа")        



list = [-1, 0, 1, 2]

try:
    test_even(list)
except EvenException as er:
    print(er) 

try:
    test_negative(list)
except NegativeException as er:
    print(er)     