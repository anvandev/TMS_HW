""" Закрепить знания по работе с функциями.
Описать функцию fact2( n ), вычисляющую двойной факториал :n!! =
1·3·5·...·n, если n — нечетное; n!! = 2·4·6·...·n, если n — четное (n > 0 —
параметр целого типа. С помощью этой функции найти двойные
факториалы пяти данных целых чисел """

from functools import reduce


numbers = [4, 6, 3, 5, 7, 3]


# function for list of numbers (old solution)
def factorial2(numbers):
    result = []
    for number in numbers:
        i = 2 if not number % 2 else 1
        result.append([number, reduce(lambda x, y: x * y, range(i, number+1, 2))])
    return result


# function for one number (old solution)
def fact2(number):
    if not number % 2:
        factorial = reduce(lambda x, y: x * y, range(2, number+1, 2))
    else:
        factorial = reduce(lambda x, y: x * y, range(1, number+1, 2))
    return factorial


print(factorial2(numbers))
for n in numbers:
    print(f'Двойной факториал {n} = {fact2(n)}.')
