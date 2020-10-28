"""
Калькулятор построен на алгоритме пинг-понг.
Калькулятор работает для целых, дробных, неотрицательных и отрицательных чисел.
Отрицательные числа должны быть записаны в виде (-34).
Допустимые операции: **, *, /, +, -. Пробелы значение не имеют.
Можно использовать скобки (20 любых выражений в скобках,
для изменения кол-ва - см. ограничение j в цикле функции calculate_and_print).

Пример выражения: ( (-2.3) + 3 ** (2 - 2)) * 2.2 + (6/(3 + 3)* (-2)) ** 2
При вводе некорректного выражения прерывает выполнение и выводит сообщение.

сделать: 1.пофиксить ограничение в 20 выражений, (raise, цикл for ... )
2. почистить код + написать с применением ООП
"""


def math_operation(expression):
    """ simple calculator for two numbers in expression like 3 + 3 """
    if not str(expression[0]).isdigit() or not str(expression[2]).isdigit():
        # исключает вызов ошибки при дробных и отрицательных числах
        if not str(expression[0]).replace('.', '1').replace('-', '1').isdigit() or \
                not str(expression[2]).replace('.', '1').replace('-', '1').isdigit():
            print(f'{expression} - check your expression, something wrong')
            raise SystemExit(5)
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


def ping_calculate_pong(expression, operator_index):
    """
    argument 1: an expression from which we will extract one subexpression
    argument 2: the index of the mathematical operator around which function takes the subexpression to extract
    Function: 1. takes the expression and extract one subexpression around math operator (like 2 + 2) - ping;
      2. calculates subexpression result using "math_operation" function;
      3. replace in expression: subexpression to subexpression result - pong.
    """
    if len(expression) < 3 or operator_index == len(expression)-1 or operator_index == 0:
        print(f'{expression} - check your expression, something wrong')
        raise SystemExit(4)
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
    j = 1  # защита от вечного цикла при неотловленных ошибках ввода
    while j < 22:
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
                        print(f'{fr_result} - check your expression, something wrong')
                        raise SystemExit(3)
                    expression[z] = fr_result[0]
                    del expression[a:z]
                else:
                    print('check your expression, something wrong with parentheses')
                    raise SystemExit(2)
            else:
                print('check your expression, something wrong with parentheses')
                raise SystemExit(2)
        else:
            expression = calculator_without_parentheses(expression)
        j += 1
    if len(expression) != 1:
        print(f'{expression} - something wrong, return raise SystemExit(3) ')
        # raise SystemExit(3)  # 'это вот возможно лишнее уже
    if len(expression) == 1:
        print(f'result: {expression[0]}')


# input expression and convert to the list
exp_input = list(input(f'Input math expression: '))

# clear the list of spaces
exp_clear = list(filter(lambda x: x != ' ', exp_input))

# checks characters in an expression for correctness
check_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', '*', '/', '(', ')', '.']
for element in exp_clear:
    if element not in check_list:
        print(f'Houston, we have a problem. Element {element} in expression is not correct.')
        raise SystemExit(1)

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
        print(f'{exp_num} - check your expression, something wrong')
        raise SystemExit(12)

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
