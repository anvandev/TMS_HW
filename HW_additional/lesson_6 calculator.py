""" пока что калькулятор может:
1. принимать введенное выражение,
2. очищать выражение от пробелов
3. определять многозначные числа в выражении и переводить их в int

далее:
применить алгоритм пинг-понг
4. прописать функции для операций +- */ ** с 2 числами
5. написать калькулятор для выражений с множестом числел - с операциями одного уровня (без скобок)
6. калькулятор с операциями разного уровня (без скобок)
7. калькулятор со скобками + с пониманием отрицательных числе в виде (-3)
8. почистить код + написать с применением ООП
"""


# input expression and convert to the list
exp_input = list(input(f'Input math expression: '))
# print(exp_input)


# clear the list of spaces
exp_clear = list(filter(lambda x: x != ' ', exp_input))
# print(exp_clear)


# find multi-digit numbers and create new list with int
exp = []
i = 0
while i < len(exp_clear):
    number = ''
    while i < len(exp_clear) and exp_clear[i].isdigit():
        number += exp_clear[i]
        if i+1 == len(exp_clear) or not exp_clear[i+1].isdigit():
            exp.append(int(number))
        i += 1
    if i < len(exp_clear):
        exp.append(exp_clear[i])
    i += 1
print(exp)
