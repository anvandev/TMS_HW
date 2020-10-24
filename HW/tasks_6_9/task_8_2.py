""" Закрепить знания по работе с функциями.
Даны три слова. Выяснить, является ли хоть одно из них палиндромом
("перевертышем"), т. е. таким, которое читается одинаково слева направо и
справа налево. (Определить функцию, позволяющую распознавать слова
палиндромы.) """


def palindrome(n):
    if n == n[::-1]:
        result = 'palindrome'
    else:
        result = 'not palindrome'
    return result


words = ['tenet', 'level', 'moon']

for word in words:
    print(f'{word} - {palindrome(word)}')
