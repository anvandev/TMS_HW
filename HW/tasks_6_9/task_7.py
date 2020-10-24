""" Закрепить базовые знания по работе с функциями.
7.1. Написать 12 функций по переводу.
7.2. Написать программу, со следующим интерфейсом: пользователю предоставляется на
выбор 12 вариантов перевода(описанных в первой задаче). Пользователь вводит цифру
от одного до двенадцати. После программа запрашивает ввести численное значение.
Затем программа выдает конвертированный результат. Использовать функции из первого
задания. Программа должна быть в бесконечном цикле. Код выхода из программы - “0”."""


def in_cm(x):
    """ 1. convert inches to centimeters """
    return x * 2.54


def cm_in(x):
    """ 2. convert centimeters to inches """
    return x * 0.393701


def mile_km(x):
    """ 3. convert miles to kilometers """
    return x * 1.60934


def km_mile(x):
    """ 4. convert kilometers to miles """
    return x * 0.621371


def lb_kg(x):
    """ 5. convert pounds to kilograms """
    return x * 0.453592


def kg_lb(x):
    """ 6. convert kilograms to pounds"""
    return x * 2.20462


def oz_gm(x):
    """ 7. convert ounces to grams """
    return x * 28.3495


def gm_oz(x):
    """ 8. convert grams to ounces """
    return x * 0.035274


def gal_l(x):
    """ 9. convert gallons to liters """
    return x * 3.78541


def l_gal(x):
    """ 10. convert liters to gallons """
    return x * 0.264172


def pt_l(x):
    """ 11. convert pints to liters """
    return x * 0.473176


def l_pt(x):
    """ 12. convert liters to pints """
    return x * 2.11338


print('''12 функций по переводу:
1. Дюймы в сантиметры
2. Сантиметры в дюймы
3. Мили в километры
4. Километры в мили
5. Фунты в килограммы
6. Килограммы в фунты
7. Унции в граммы
8. Граммы в унции
9. Галлон в литры
10. Литры в галлоны
11. Пинты в литры
12. Литры в пинты 
''')

# 1 version of the program
while True:
    f_number = int(input('Введите № функции: '))
    if f_number > 12 or f_number < 0:
        print('Введите корректный № функции.')
    if f_number == 0:
        break
    if 1 <= f_number <= 12:
        q = int(input('Введите кол-во для перевода: '))
        program_list = [in_cm(q), cm_in(q), mile_km(q), km_mile(q), lb_kg(q), kg_lb(q),
                        oz_gm(q), gm_oz(q), gal_l(q), l_gal(q), pt_l(q), l_pt(q)]
        print(f'Результат: {program_list[f_number-1]}')


# 2 version of the program
# while True:
#     f_number = int(input('Введите № функции: '))
#     if f_number > 12 or f_number < 0:
#         print('Введите корректный № функции.')
#     if f_number == 0:
#         break
#     if 1 <= f_number <= 12:
#         quantity = int(input('Введите кол-во для перевода: '))
#         if f_number == 1:
#             print(f'Результат: {in_cm(quantity)} см')
#         elif f_number == 2:
#             print(f'Результат: {cm_in(quantity)}')
#         elif f_number == 3:
#             print(f'Результат: {mile_km(quantity)} км')
#         elif f_number == 4:
#             print(f'Результат: {km_mile(quantity)}')
#         elif f_number == 5:
#             print(f'Результат: {lb_kg(quantity)} кг')
#         elif f_number == 6:
#             print(f'Результат: {kg_lb(quantity)}')
#         elif f_number == 7:
#             print(f'Результат: {oz_gm(quantity)} гр')
#         elif f_number == 8:
#             print(f'Результат: {gm_oz(quantity)}')
#         elif f_number == 9:
#             print(f'Результат: {gal_l(quantity)} л')
#         elif f_number == 10:
#             print(f'Результат: {l_gal(quantity)}')
#         elif f_number == 11:
#             print(f'Результат: {pt_l(quantity)} л')
#         elif f_number == 12:
#             print(f'Результат: {l_pt(quantity)}')
