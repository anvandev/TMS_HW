"""Закрепить знания по работе с условным оператором if/elif/else.
Введите число. Если это число делится на 1000 без остатка, то выведите на
экран "millennium" """

number = int(input("Number: "))

# using ternary operator
print('millennium' if number % 1000 == 0 else None)

# using simple if statement
if number % 1000 == 0:
    print("millennium")
