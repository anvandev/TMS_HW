""" Закрепить знания по работе с lambda функциями, генераторами списков и словарей,
декораторами.
Создать универсальный декоратор, который меняет порядок аргументов в
функции на противоположный. """


# version 1 - декоратор для функции с любым кол-вом агрументов
def mirror_arguments(func):
    def wrapper(*args):
        args = list(args)
        i = len(args) - 1
        new_args = []
        while i >= 0:
            new_args.append(args[i])
            i -= 1
        return func(*new_args)
    return wrapper

# version 2 - декоратор для функции с 2 аргументами
# def mirror_arguments(func):
#     def wrapper(arg1, arg2):
#         return func(arg2, arg1)
#     return wrapper


@mirror_arguments
def join_and(x, y):
    return f'{x} and {y}'


@mirror_arguments
def minus(x, y, z):
    return x - y - z


print(join_and('sun', 'stars'))
print(minus(10, 5, 1))
