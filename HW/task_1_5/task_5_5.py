""" Закрепить знания по работе с циклами и условиями.
В массиве целых чисел с количеством элементов 19 определить максимальное
число и заменить им все четные по значению элементы."""


from array import array


numbers = array('i', [3, 6, 8, 3, 7, 9, 5, 20, 32, 2, 9, 33, 41, 3, 6, 8, 13, 2, 17])
n_max = max(numbers)
print(f'Maximum number: {n_max}')


# using list comprehension with ternary operator
new_numbers = array('i', [n_max if not num % 2 else num for num in numbers])
print(new_numbers)


# using for loop
for index, num in enumerate(numbers):
    if not num % 2:
        numbers[index] = n_max
print(numbers)


# 2 version - using while loop (old)
# i = 0
# while i < len(numbers):
#     if numbers[i] % 2 == 0:
#         numbers[i] = n_max
#     i += 1
# print(numbers)
