""" Закрепить знания по работе с условным оператором if/elif/else.
Ввести строку. Если длина строки больше 10 символов, то создать новую
строку с 3 восклицательными знаками в конце ('!!!') и вывести на экран.
Если меньше 10, то вывести на экран второй символ строки """

string = input('Input something: ')

# using ternary operator
print(f'{string}!!!' if len(string) > 10 else string[1])

# using simple if statement
if len(string) > 10:
    new_string = f'{string}!!!'
    print(new_string)
else:
    print(string[1])
