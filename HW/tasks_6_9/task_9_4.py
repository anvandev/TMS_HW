""" Закрепить знания по работе с lambda функциями, генераторами списков и словарей,
декораторами.
Создать универсальный декоратор, который меняет порядок аргументов в
функции на противоположный. """


# version 1 - декоратор для функции с любым кол-вом агрументов
def mirror_arguments(func):
    def wrapper(*args):
        reverse_args = args[::-1]
        return func(*reverse_args)
    return wrapper


@mirror_arguments
def join_and(x, y):
    return f'{x} and {y}'


@mirror_arguments
def minus(x, y, z):
    return x - y - z


print(join_and('sun', 'stars'))
print(minus(10, 5, 1))
