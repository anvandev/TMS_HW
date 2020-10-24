""" Закрепить знания по работе с циклами. Составить список чисел Фибоначчи содержащий 15 элементов.
(Подсказка: Числа Фибоначчи - последовательность, в которой первые два числа равны
либо 1 и 1, а каждое последующее число равно сумме двух предыдущих чисел.
Пример: 1, 1, 2, 3, 5, 8, 13, 21, 34... ) """


# using while loop
l_fib = []
i = 0
while len(l_fib) < 15:
    while len(l_fib) < 2:
        l_fib.append(1)
    next_num = l_fib[i] + l_fib[i+1]
    l_fib.append(next_num)
    i += 1
print(l_fib)


# using for loop
l_fib = []
i = 0
if len(l_fib) == 0:
    l_fib.append(1)
    l_fib.append(1)
for n in l_fib:
    next_num = l_fib[i] + l_fib[i+1]
    l_fib.append(next_num)
    i += 1
    if len(l_fib) == 15:
        break
print(l_fib)
