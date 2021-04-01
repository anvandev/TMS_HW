""" Закрепить знания по работе с циклами.
Дан список целых чисел. Создать новый список,
каждый элемент которого равен исходному элементу
умноженному на -2 """

numbers = [2, 6, 3, -10, 14, 7]

# using generator expressions
new_numbers = [x * -2 for x in numbers]
print(new_numbers)


# using for loop
new_numbers = []
for number in numbers:
    new_numbers.append(number * -2)
print(new_numbers)


# using while loop
new_numbers = []
i = 0
while i < len(numbers):
    new_numbers.append(numbers[i] * -2)
    i += 1
print(new_numbers)
