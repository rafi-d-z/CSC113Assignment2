# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math

def greet(name: str):
    print("Hello, " + name + "!")


def calculate_area(length: int, width: int):
    return length * width


def calculate_volume(length: int, width: int, height: int):
    return calculate_area(length, width) * height


def is_even(number: int):
    x = number % 2 == 0
    return x


def factorial(n: int):
    if n == 1:
        return n
    else:
        return n * factorial(n - 1)


def get_average(l: list):
    n = sum(l)
    return n / len(l)


def get_median(l: list):
    l1 = sorted(l)
    if is_even(len(l)):
        return l1[len(l)//2]
    else:
        x = l1[math.floor(len(l)/2)] + l1[math.ceil(len(l)/2)]
        return x/2



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    greet("Rafid")
    print(calculate_area(5, 3))
    print(is_even(7))
    print(is_even(6))
    print(is_even(42))
    print(is_even(69))
    print(calculate_volume(4, 3, 2))
    print(factorial(5))

    list_of_numbers = [13, 56, 40, 27, 89, 45]
    print(get_average(list_of_numbers))
    print(get_median(list_of_numbers))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
