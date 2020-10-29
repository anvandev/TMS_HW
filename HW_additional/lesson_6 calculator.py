"""
Калькулятор построен на алгоритме пинг-понг.
Калькулятор работает для целых, дробных, неотрицательных и отрицательных чисел.
Отрицательные числа должны быть записаны в виде (-34).
Допустимые операции: **, *, /, +, -. Можно использовать скобки. Пробелы значение не имеют.

Пример выражения: ( (-2.3) + 3 ** (2 - 2)) * 2.2 + (6/(3 + 3)* (-2)) ** 2
При вводе некорректного выражения, прерывает выполнение и выводит сообщение.

сделать: улучшить код + написать с применением ООП
"""


def math_operation(expression):
    """ simple calculator for two numbers in expression like 3 + 3 """
    if not str(expression[0]).isdigit() or not str(expression[2]).isdigit():
        # исключает вызов ошибки при дробных и отрицательных числах
        if not str(expression[0]).replace('.', '1').replace('-', '1').isdigit() or \
                not str(expression[2]).replace('.', '1').replace('-', '1').isdigit():
            raise SystemExit(f'error-8: {expression} - check your expression, something wrong')
    if expression[2] == 0 and expression[1] == '/':
        raise SystemExit(f'error-9: {expression} - division by zero in expression')
    operator = expression[1]
    if operator == '**':
        return expression[0]**expression[2]
    elif operator == '*':
        return expression[0]*expression[2]
    elif operator == '/':
        return expression[0]/expression[2]
    elif operator == '+':
        return expression[0]+expression[2]
    elif operator == '-':
        return expression[0]-expression[2]
    # x, y = 1, 1
    # operations_list = {'**': x**y, '*': x*y, '/': x/y, '+': x+y, '-': x-y}
    # x, y = expression[0], expression[2]
    # return operations_list[expression[1]]


def ping_calculate_pong(expression, operator_index):
    """
    argument 1: an expression from which we will extract one subexpression
    argument 2: the index of the mathematical operator around which function takes the subexpression to extract
    Function: 1. takes the expression and extract one subexpression around math operator (like 2 + 2) - ping;
      2. calculates subexpression result using "math_operation" function;
      3. replace in expression: subexpression to subexpression result - pong.
    """
    if len(expression) < 3 or operator_index == len(expression)-1 or operator_index == 0:
        raise SystemExit(f'error-7: {expression} - check your expression, something wrong')
    sub_expression = expression[operator_index - 1:operator_index + 2]
    sub_result = math_operation(sub_expression)
    expression[operator_index+1] = sub_result
    del expression[operator_index-1:operator_index+1]


def calculator_without_parentheses(expression):
    """
    argument - expression to count
    function prioritizes mathematical operations and applies function "ping_calculate_pong"
    returns expression with result
    """
    j = 1
    while len(expression) > j:
        if "**" in expression:
            ping_calculate_pong(expression, expression.index('**'))
        elif '*' in expression or '/' in expression:
            if '*' in expression and '/' in expression:
                if expression.index('*') < expression.index('/'):
                    ping_calculate_pong(expression, expression.index('*'))
                else:
                    ping_calculate_pong(expression, expression.index('/'))
            elif '/' not in expression:
                ping_calculate_pong(expression, expression.index('*'))
            elif '*' not in expression:
                ping_calculate_pong(expression, expression.index('/'))
        elif '+' in expression or '-' in expression:
            if '+' in expression and '-' in expression:
                if expression.index('+') < expression.index('-'):
                    ping_calculate_pong(expression, expression.index('+'))
                else:
                    ping_calculate_pong(expression, expression.index('-'))
            elif '-' not in expression:
                ping_calculate_pong(expression, expression.index('+'))
            elif '+' not in expression:
                ping_calculate_pong(expression, expression.index('-'))
        else:
            j += 1  # защита от возможного вечного цикла, при вводе некорректного выражения
    return expression


def calculate_and_print(expression):
    for el in expression.copy():
        if ')' in expression:
            if '(' in expression:
                if expression.index(')') > expression.index('('):
                    z = expression.index(')')
                    a = z
                    while expression[a] != '(':
                        a -= 1
                    fragment = expression[a+1:z]
                    fr_result = calculator_without_parentheses(fragment)
                    if len(fr_result) != 1:  # проверка на наличие ошибки ввода в фрагменте выражения ((()))
                        raise SystemExit(f'error-4: {fr_result} - check your expression, something wrong')
                    expression[z] = fr_result[0]
                    del expression[a:z]
                else:
                    raise SystemExit('error-5: check your expression, something wrong with parentheses')
            else:
                raise SystemExit('error-5: check your expression, something wrong with parentheses')
        else:
            expression = calculator_without_parentheses(expression)
    if len(expression) != 1:
        raise SystemExit(f'error-6: {expression} - check your expression, something wrong')
    if len(expression) == 1:
        print(f'result: {expression[0]}')


# input expression, clear of spaces and convert to the list
exp_clear = list(filter(lambda x: x != ' ', input(f'Input math expression: ')))

# check characters in an expression for correctness
check_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', '*', '/', '(', ')', '.']
for element in exp_clear:
    if element not in check_list:
        raise SystemExit(f'error-1: Houston, we have a problem. Element {element} in expression is not correct.')

# find multi-digit numbers and create new list with int
exp_num = []
i = 0
while i < len(exp_clear):
    number = ''
    while i < len(exp_clear) and exp_clear[i].isdigit():
        number += exp_clear[i]
        if i+1 == len(exp_clear) or not exp_clear[i+1].isdigit():
            exp_num.append(int(number))
        i += 1
    if i < len(exp_clear):
        exp_num.append(exp_clear[i])
    i += 1

# find fractional (float) numbers and update list
while'.' in exp_num:
    if exp_num.index('.') != len(exp_num)-1 and exp_num.index('.') != 0 \
            and type(exp_num[exp_num.index('.')-1]) == int and type(exp_num[exp_num.index('.')+1]) == int:
        fl_number = float(str(exp_num[exp_num.index('.')-1]) + exp_num[exp_num.index('.')] +
                          str(exp_num[exp_num.index('.')+1]))
        exp_num[exp_num.index('.')+1] = fl_number
        del exp_num[exp_num.index('.')-1:exp_num.index('.')+1]
    else:
        raise SystemExit(f'error-2: check your expression, something wrong with "."')

# find negative numbers and update list
i = 0
while '(' in exp_num and i < len(exp_num.copy()):
    if exp_num[i] == '(' and i+3 < len(exp_num) and exp_num[i+1] == '-' and exp_num[i+3] == ')':
        if type(exp_num[i+2]) == int:
            negative_number = int('-' + str(exp_num[i+2]))
            exp_num[i + 3] = negative_number
            del exp_num[i:i + 3]
        elif type(exp_num[i + 2]) == float:
            negative_number = float('-' + str(exp_num[i+2]))
            exp_num[i + 3] = negative_number
            del exp_num[i:i + 3]
        else:
            raise SystemExit(f'error-3: check your expression, something wrong with "(-?)"')
    i += 1

# find exponent operator and create new list
exp = []
i = 0
while i < len(exp_num):
    if exp_num[i] == '*' and i != len(exp_num)-1 and exp_num[i+1] == '*':
        exp.append('**')
        i += 2
    else:
        exp.append(exp_num[i])
        i += 1
# print(exp)

# apply the calculator
calculate_and_print(exp)
