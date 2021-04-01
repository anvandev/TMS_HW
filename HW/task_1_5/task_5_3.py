""" Закрепить знания по работе с циклами и условиями.
Два натуральных числа называют дружественными, если каждое из них
равно сумме всех делителей другого, кроме самого этого числа. Найти все
пары дружественных чисел, лежащих в диапазоне от 200 до 300. """

# получаем словарь с парами: {число из диапазона: сумма его целочисленных делителей}
d_sum = {}
for number in range(200, 300):
    n_sum_dividers = 0
    for divider in range(1, number):  # считаем сумму целых делителей каждого числа от 200 до 300
        if not number % divider:
            n_sum_dividers += divider
    # добавляем в словарь пару, только если сумма делителей в диапазоне от 200 до 300
    if 200 <= n_sum_dividers < 300:
        d_sum[number] = n_sum_dividers
print(d_sum)

# убираем ключи и значения, которые не встречаются
for number in d_sum.copy():
    if number not in d_sum.values() or d_sum[number] not in d_sum.keys():
        del d_sum[number]
print(d_sum)
