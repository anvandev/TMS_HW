"""Закрепить знания по работе с lambda функциями, генераторами списков и словарей,
декораторами.
Создать декоратор для функции, которая принимает список чисел. Декоратор должен производить
предварительную проверку данных - удалять все четные элементы из списка. """


# 1 version of decorator
def only_odd_numbers(func):
    def wrapper(*args):
        odd_numbers = [number for number in args if number % 2]
        return odd_numbers
    return wrapper


@only_odd_numbers
def numbers(*args):
    return list(args)


print(numbers(1, 2, 3, 5, 5, 6, 7, 4, 8, 9))
