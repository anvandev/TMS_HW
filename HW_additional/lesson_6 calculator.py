""" Алгоритм пинг-понг
пока что калькулятор может:
1. принимать введенное выражение и очищать его от пробелов
2. определять многозначные числа и знак **  и преобразование в итоговый список для вычислений
3. выполняет операций +- */ ** с 2 числами
4. калькулятор для выражений с множеством чисел - с операциями одного уровня - не понимает приоритет (без скобок)
   4.1. 1 уровень - **; 2 уровень - */; 3 уровень - +-.
   Пример: 3 + 10 - 2 или 3 * 10 / 2

далее:
5. калькулятор с операциями разного уровня - понимает приоритет (без скобок)
6. калькулятор со скобками + с пониманием отрицательных числе в виде (-3)
7. почистить код + написать с применением ООП
"""


# func - calculator for two numbers (operations: + - / * **)
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


# func - calculator for expressions with multiple numbers - with operations of the same level
# - does not understand priority
def calc_one_level(expression):
    while len(expression) > 1:
        operation = math_operation(expression)
        expression.insert(0, operation)
        del expression[2+1]
        del expression[1+1]
        del expression[0+1]
    return expression


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


# calculator for expressions with multiple numbers - with operations of the same level
# - does not understand priority
result = calc_one_level(exp)
print(f'result: {result}')
