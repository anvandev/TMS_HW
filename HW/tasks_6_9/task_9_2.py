"""Закрепить знания по работе с lambda функциями, генераторами списков и словарей,
декораторами.
Создать lambda функцию, которая принимает на вход неопределенное
количество именных аргументов и выводит словарь с ключами удвоенной
длины. {‘abc’: 5} -> {‘abcabc’: 5} """


cities = lambda **kwargs: {key + key: value for key, value in kwargs.items()}


print(cities(Tokyo=3, Singapore=4, Sydney=5))
