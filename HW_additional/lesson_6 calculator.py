""" Алгоритм пинг-понг
пока что калькулятор может:
1. принимать введенное выражение и очищать его от пробелов
2. определять многозначные числа и знак **  и преобразование в итоговый список для вычислений
3. калькулятор для выражений с операциями разного уровня - понимает приоритет (пока что без скобок)
   1 уровень - **; 2 уровень - */; 3 уровень - +-.
   Пример: 2 + 3 ** 2 - 2 * 2 + 6/3 + 3* 2 ** 2

далее:
4. проверка на непредусмотренные символы при вводе строки
5. калькулятор со скобками + с пониманием отрицательных числе в виде (-3)
6. почистить код + написать с применением ООП + raise error  при неккоректном
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
    1 аргумент: выражение, из которого мы будем вычленять одно подвыражение
    2 аргумент: индекс математического оператора, вокруг которого мы возьмем подвыражение для вычленения
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
    функция выделяет приоритеты математических операций:
    1 уровень - **; 2 уровень - */; 3 уровень - +-.
    и применяет по очереди функцию ping_calculate_pong и возвращает список с результатом
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
# добавить проверку на неправильные символы
# print(exp_input)


# clear the list of spaces
exp_clear = list(filter(lambda x: x != ' ', exp_input))


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
# print(exp)

result = calculator_without_parentheses(exp)
print(result)
if len(result) == 1:
    print(f'result: {result[0]}')
