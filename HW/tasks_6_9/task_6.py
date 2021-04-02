"""Закрепить знания по работе git. Примечание:Все задания выполнять в Одном файле друг
за другом. Каждое задание - отдельный коммит. Итоговый файл должен
содержать все решения всех задач. Все действия выполняются с матрицей из первого задания.
1) Создать матрицу случайных чисел от a до b, размерность матрицы n*m
2) Найти максимальный элемент матрицы.
3) Найти минимальный минимальный матрицы.
4) Найти сумму всех элементов матрицы.
5) Найти индекс ряда с максимальной суммой элементов.
6) Найти индекс колонки с максимальной суммой элементов.
7) Найти индекс ряда с минимальной суммой элементов.
8) Найти индекс колонки с минимальной суммой элементов.
9) Обнулить все элементы выше главной диагонали.
10) Обнулить все элементы ниже главной диагонали.
11) Создать две новые матрицы matrix_a, matrix_b случайных чисел размерностью n*m.
12)Создать матрицу равную сумме matrix_a и matrix_b.
13)Создать матрицу равную разности matrix_a и matrix_b.
14)Создать новую матрицу равную matrix_a умноженной на g. g вводится с клавиатура"""

from random import randint
from functools import reduce


def print_matrix(matrix):
    for line in matrix:
        print(line)


# 1) Создать матрицу случайных чисел от a до b, размерность матрицы n*m
n = 4
m = 4
random_matrix = [[randint(1, 9) for i in range(n)] for j in range(m)]
print_matrix(random_matrix)

# 2) Найти максимальный элемент матрицы. - разделить на два коммита
# 3) Найти минимальный элемент матрицы.
max_element = max(map(max, random_matrix))
print(f'Максимальный элемент -  {max_element}')
min_element = min(map(min, random_matrix))
print(f'Минимальный элемент - {min_element}')

# 4) Найти сумму всех элементов матрицы.
sum_elements_in_line = list(map(sum, random_matrix))
sum_all_elements = sum(sum_elements_in_line)
print(f'Сумма всех элементов - {sum_all_elements}')

# 5) Найти индекс ряда с максимальной суммой элементов.
line_index_max_sum = sum_elements_in_line.index(max(sum_elements_in_line))
print(f'Индекс ряда с максимальной суммой элементов - {line_index_max_sum}')

# 7) Найти индекс ряда с минимальной суммой элементов.
line_index_min_sum = sum_elements_in_line.index(min(sum_elements_in_line))
print(f'Индекс ряда с минимальной суммой элементов - {line_index_min_sum}')

# 6) Найти индекс колонки с максимальной суммой элементов.
# 8) Найти индекс колонки с минимальной суммой элементов.
a, b, c, d = random_matrix
sum_elements_in_column = list(map(sum, zip(a, b, c, d)))

column_index_max_sum = sum_elements_in_column.index(max(sum_elements_in_column))
print(f'Индекс колонки с максимальной суммой элементов - {column_index_max_sum}')

column_index_min_sum = sum_elements_in_column.index(min(sum_elements_in_column))
print(f'Индекс колонки с минимальной суммой элементов - {column_index_min_sum}')

# 9) Обнулить все элементы выше главной диагонали.
# first solution
matrix_0_above = []
for i, line in enumerate(random_matrix):
    new_line = [number if j <= i else 0 for j, number in enumerate(line)]
    matrix_0_above.append(new_line)

# # second solution
# matrix_0_above = [[number if j <= i else 0 for j, number in enumerate(line)] for i, line in enumerate(random_matrix)]
print(f'Matrix with 0 above main diagonal:')
print_matrix(matrix_0_above)

# 10) Обнулить все элементы ниже главной диагонали.
# first solution
matrix_0_below = []
for i, line in enumerate(random_matrix):
    new_line = [number if j >= i else 0 for j, number in enumerate(line)]
    matrix_0_below.append(new_line)

# # second solution
# matrix_0_below = [[number if j >= i else 0 for j, number in enumerate(line)] for i, line in enumerate(random_matrix)]
print(f'Matrix with 0 below main diagonal:')
print_matrix(matrix_0_below)

# 11) Создать две новые матрицы matrix_a, matrix_b случайных чисел размерностью n*m.
matrix_a = [[randint(1, 9) for f in range(n)] for g in range(m)]
matrix_b = [[randint(1, 9) for f in range(n)] for g in range(m)]

print(f'Matrix a:')
print_matrix(matrix_a)

print(f'Matrix b:')
print_matrix(matrix_b)


# 12)Создать матрицу равную сумме matrix_a и matrix_b.
# first solution
matrix_a_plus_b = [[a + b for a, b in zip(line_a, line_b)] for line_a, line_b in zip(matrix_a, matrix_b)]

# # second solution
# matrix_a_plus_b = []
# for i, line in enumerate(matrix_a):
#     new_line = [number + matrix_b[i][j] for j, number in enumerate(line)]
#     matrix_a_plus_b.append(new_line)
print('Matrix a + matrix b: ')
print_matrix(matrix_a_plus_b)


# 13)Создать матрицу равную разности matrix_a и matrix_b.
# first solution
matrix_a_plus_b = [[a - b for a, b in zip(line_a, line_b)] for line_a, line_b in zip(matrix_a, matrix_b)]

# # second solution
matrix_a_minus_b = []
for i, line in enumerate(matrix_a):
    new_line = [number - matrix_b[i][j] for j, number in enumerate(line)]
    matrix_a_minus_b.append(new_line)
print('Matrix a - matrix b: ')
print_matrix(matrix_a_minus_b)


# 14)Создать новую матрицу равную matrix_a умноженной на g. g вводится с клавиатуры"""
g = int(input('Введите значение g: '))
matrix_a_mult_g = [[n * g for n in line] for line in matrix_a]
print_matrix(matrix_a_mult_g)
