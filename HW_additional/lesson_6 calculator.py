""" пока что калькулятор может:
1. принимать введенное выражение и очищать его от пробелов
3. определять многозначные числа и знак **  и преобразование в итоговый список для вычислений
5. выполняет операций +- */ ** с 2 числами

далее:
применить алгоритм пинг-понг
5. написать калькулятор для выражений с множестом числел - с операциями одного уровня (без скобок)
6. калькулятор с операциями разного уровня (без скобок)
7. калькулятор со скобками + с пониманием отрицательных числе в виде (-3)
8. почистить код + написать с применением ООП
"""


# calculator for two numbers
def math_operation(expression):
    operator = expression[1]
    if operator == '**':
        return expression[0]**expression[2]
    if operator == '*':
        return expression[0]*expression[2]
    if operator == '/':
        return expression[0]/expression[2]
    if operator == '+':
        return expression[0]+expression[2]
    if operator == '-':
        return expression[0]-expression[2]


# input expression and convert to the list
exp_input = list(input(f'Input math expression: '))
# print(exp_input)


# clear the list of spaces
exp_clear = list(filter(lambda x: x != ' ', exp_input))
# print(exp_clear)


# find multi-digit numbers and create new list with int
exp_int = []
i = 0
while i < len(exp_clear):
    number = ''
    while i < len(exp_clear) and exp_clear[i].isdigit():
        number += exp_clear[i]
        if i+1 == len(exp_clear) or not exp_clear[i+1].isdigit():
            exp_int.append(int(number))
        i += 1
    if i < len(exp_clear):
        exp_int.append(exp_clear[i])
    i += 1
# print(exp_int)


# find exponentation operator and create new list
exp = []
i = 0
while i < len(exp_int):
    if exp_int[i] == '*' and exp_int[i+1] == '*':
        exp.append('**')
        i += 2
    else:
        exp.append(exp_int[i])
        i += 1
print(exp)


# calculator for two numbers (operations: + - / * **)
print(math_operation(exp))
