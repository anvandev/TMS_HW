""" Закрепить знания по работе с циклами и условиями.
Дано число. Найти сумму и произведение его цифр. """

number = abs(12345)
num_iter = str(number)
n_sum = 0
n_mul = 1

# var 1
for n in num_iter:
    n_sum += int(n)
    n_mul *= int(n)

# var 2
# for i in str(num_iter):
#     n = number % 10
#     n_sum += n
#     n_mul *= n
#     number //= 10

print(f'summ = {n_sum}')
print(f'multiplication = {n_mul}')
