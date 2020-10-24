"""Закрепить знания по работе с условным оператором if/elif/else.
Введите число. Если это число делится на 1000 без остатка, то выведите на
экран "millennium" """

number = int(input("Number: "))
if number % 1000 == 0:
    print("millennium")
