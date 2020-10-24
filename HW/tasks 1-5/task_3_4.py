""" Закрепить знания по работе с условным оператором if/elif/else.
Ввести строку. Вывести на экран букву, которая находится в середине этой
строки. Также, если эта центральная буква равна первой букве в строке, то создать и
вывести часть строки между первым и последним символами исходной строки. """

string = input('Input something: ')
length = len(string)
if length % 2 != 0:
    print(string[length//2])
    if string[length//2] == string[0]:
        print(string[1:-1])
else:
    print('no middle letter')
