""" Закрепить знания по работе с циклами и условиями.
Дано число. Найти сумму и произведение его цифр. """

number = 12345

num_iter = str(number)
n_sum = 0
n_mul = 1

for n in num_iter:
    n_sum += int(n)
    n_mul *= int(n)

print(f'summ = {n_sum}')
print(f'multiplication = {n_mul}')
