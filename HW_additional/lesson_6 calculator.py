"""
Калькулятор построен на алгоритме пинг-понг.
Калькулятор пока что работает для целых неотрицательных чисел.
Допустимые операции: **, *, /, +, -. Пробелы значение не имеют.
Пример: 2 + 3 ** 2 - 2 * 2 + 6/3 + 3* 2 ** 2

далее сделать:
4. калькулятор со скобками
4. калькулятор с пониманием отрицательных числе в виде (-3) и дробных чисел
5. почистить код + написать с применением ООП + raise error  при неккоректном
вводе символов (два оператора подряд, два числа and so on)
"""


def math_operation(expression):
    """ calculator for two numbers in expression like 3 + 3 (operations: + - / * **) """
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


def ping_calculate_pong(expression, operator_index):
    """
    argument 1: an expression from which we will extract one subexpression
    argument 2: the index of the mathematical operator around which we will take the subexpression to extract
    Алгоритм действия:
    1. Вычленяем из выражения наше подвыражение
    2. Вычисляем результат подвыражения функцией math_operation
    3. В главном выражении заменяем подвыражение результатом
    """
    sub_expression = expression[operator_index - 1:operator_index + 2]
    sub_result = math_operation(sub_expression)
    expression.insert(operator_index + 2, sub_result)
    del expression[operator_index + 1]
    del expression[operator_index]
    del expression[operator_index - 1]


def calculator_without_parentheses(expression):
    """
    аргумент - выражение для подсчета
    функция выделяет приоритеты математических операций,
    применяет по очереди функцию ping_calculate_pong и возвращает список с результатом
    """
    j = 1
    while len(expression) > j:
        if "**" in expression:
            index = expression.index('**')
            ping_calculate_pong(expression, index)
        elif '*' in expression or '/' in expression:
            if '*' in expression and '/' in expression:
                if expression.index('*') < expression.index('/'):
                    index = expression.index('*')
                    ping_calculate_pong(expression, index)
                else:
                    index = expression.index('/')
                    ping_calculate_pong(expression, index)
            elif '/' not in expression:
                index = expression.index('*')
                ping_calculate_pong(expression, index)
            elif '*' not in expression:
                index = expression.index('/')
                ping_calculate_pong(expression, index)
        elif '+' in expression or '-' in expression:
            if '+' in expression and '-' in expression:
                if expression.index('+') < expression.index('-'):
                    index = expression.index('+')
                    ping_calculate_pong(expression, index)
                else:
                    index = expression.index('-')
                    ping_calculate_pong(expression, index)
            elif '-' not in expression:
                index = expression.index('+')
                ping_calculate_pong(expression, index)
            elif '+' not in expression:
                index = expression.index('-')
                ping_calculate_pong(expression, index)
        else:
            j += 1  # защита от возможного вечного цикла, при вводе некорректного выражения
    return expression


# input expression and convert to the list
exp_input = list(input(f'Input math expression: '))

# clear the list of spaces
exp_clear = list(filter(lambda x: x != ' ', exp_input))

# checks characters in an expression for correctness
check_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', '*', '/', '(', ')']
for element in exp_clear:
    if element not in check_list:
        print(f'Houston, we have a problem. Element {element} in expression is not correct.')


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
# print(exp)

# apply the calculator
result = calculator_without_parentheses(exp)

if len(result) != 1:
    print(f'{result} - check your expression, something wrong')
if len(result) == 1:
    print(f'result: {result[0]}')
