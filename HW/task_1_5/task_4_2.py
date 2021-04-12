""" Закрепить знания по работе с циклами.
Дан список целых чисел. Подсчитать сколько четных чисел в списке """

numbers = [2, 3, 43, -21, 10, 17, 54]

# using list comprehension
q = len([x for x in numbers if x % 2 == 0])
print(q)


# using for loop
q_even_num = 0
for number in numbers:
    if number % 2 == 0:
        q_even_num += 1
print(q_even_num)


# using while loop
q_even_num = 0
i = 0
while i < len(numbers):
    if numbers[i] % 2 == 0:
        q_even_num += 1
    i += 1
print(q_even_num)
