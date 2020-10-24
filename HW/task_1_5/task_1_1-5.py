""" Закрепить знания по работе с переменными числового типа.
Все начальные данные задаются произвольно. """


# task 1 - Даны 2 действительных числа a и b. Получить их сумму, разность и произведение.
a = 12
b = 3
print(a + b)
print(a - b)
print(a * b)


# task 2 - Даны действительные числа x и y. Получить (|x | − | y |) / (1 + | xy |)
x = -10
y = 5
print((abs(x) - abs(y)) / (1 + abs(x * y)))


# task 3 - Дана длина ребра куба. Найти объем куба и площадь его боковой поверхности.
length_cube_edge = 3

v_cube = length_cube_edge ** 3
one_plane_area = length_cube_edge ** 2
print(f'cube volume = {v_cube}')
print(f'plane area = {one_plane_area}')


# task 4 - Даны два действительных числа. Найти среднее арифметическое и
# среднее геометрическое этих чисел
a = 8
b = 2
print((a + b) / 2)
print((a * b) ** 0.5)


# task 5 - Даны катеты прямоугольного треугольника. Найти его гипотенузу и площадь.
a = 3
b = 4

hypotenuse = (a**2 + b**2)**0.5
half_p = (a + b + hypotenuse) / 2
area = (half_p * (half_p - a) * (half_p - b) * (half_p - hypotenuse))**0.5
print(f'hypotenuse = {hypotenuse}')
print(f'area = {area}')
