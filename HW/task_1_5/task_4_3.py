""" Закрепить знания по работе с циклами.
Дан словарь: {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
Добавить каждому ключу число равное длине этого ключа (пример {‘key’: ‘value’} -> {‘key3’:
‘value’}). Чтобы получить список ключей - использовать метод .keys() """

# using for loop - без метода keys - зачем он тут?
d = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
for key in d.copy():
    d[key + str(len(key))] = d[key]
    del d[key]
print(d)


# using while loop - c методом keys
d = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
keys = list(d.keys())
i = 0
while i < len(d.copy()):
    d[keys[i] + str(len(keys[i]))] = d[keys[i]]
    del d[keys[i]]
    i += 1
print(d)


# using dictionary comprehension
d = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
new_d = {key + str(len(key)): value for key, value in d.items()}
print(new_d)
