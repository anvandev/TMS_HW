""" Закрепить знания по работе с циклами и условиями.
Для каждого натурального числа в промежутке от m до n вывести все делители,
кроме единицы и самого числа. m и n вводятся с клавиатуры.
Пример:m =100, n = 105
100: 2 4 5 10 20 25 50
101:
102: 2 3 6 17 34 51
103:
104: 2 4 8 13 26 52
105: 3 5 7 15 21 35 """

m = int(input('Введите натуральное число m: '))
n = int(input('Введите натуральное число n: '))
if n > m:
    numbers = list(range(m, n + 1))
else:
    numbers = list(range(n, m + 1))

# first solution
numbers_dividers = {number: [n for n in range(2, number) if not number % n] for number in numbers}
print(numbers_dividers)

# old solution
# for n in numbers:
#     dividers = []
#     i = 2
#     while i < n:
#         if n % i == 0:
#             dividers.append(str(i))
#         i += 1
#     dividers = ' '.join(dividers)
#     print(f'{n}: {dividers}')
