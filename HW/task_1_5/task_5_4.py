""" Закрепить знания по работе с циклами и условиями.
Для заданного числа N составьте программу вычисления суммы
S=1+1/2+1/3+1/4+...+1/N, где N – натуральное число. """

# using generator expressions
n = 5
s = sum([1 / number for number in range(1, n+1)])
print(s)

# using simple for loop
n = 5
s = 0
for number in range(1, n+1):
    s += 1 / number
print(s)
