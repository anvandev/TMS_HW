"""Закрепить знания по работе с lambda функциями, генераторами списков и словарей,
декораторами.
Создать декоратор для функции, которая принимает список чисел. Декоратор должен производить
предварительную проверку данных - удалять все четные элементы из списка. """


# 1 version of decorator
def only_odd_numbers(func):
    def wrapper(*args):
        odd_numbers = func(*args)
        for n in odd_numbers.copy():
            if n % 2 == 0:
                odd_numbers.remove(n)
        return odd_numbers
    return wrapper


# 2 version of decorator
# def only_odd_numbers(func):
#     def wrapper(*args):
#         odd_numbers = []
#         for n in args:
#             if n % 2 != 0:
#                 odd_numbers.append(n)
#         return odd_numbers
#     return wrapper


@only_odd_numbers
def numbers(*args):
    return list(args)


print(numbers(1, 2, 3, 5, 5, 6, 7, 4, 8, 9))
