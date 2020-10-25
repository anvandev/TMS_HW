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
max_elements = []
min_elements = []
for line in random_matrix:
    max_elements.append(max(line))
    min_elements.append(min(line))
max_element = max(max_elements)
print(f'Максимальный элемент -  {max_element}')
min_element = min(min_elements)
print(f'Минимальный элемент - {min_element}')

# 4) Найти сумму всех элементов матрицы.
sum_elements_in_line = []
for line in random_matrix:
    sum_elements_in_line.append(sum(line))
sum_elements = sum(sum_elements_in_line)
print(f'Сумма всех элементов - {sum_elements}')

# 5) Найти индекс ряда с максимальной суммой элементов.
line_index_max_sum = sum_elements_in_line.index(max(sum_elements_in_line))
print(f'Индекс ряда с максимальной суммой элементов - {line_index_max_sum}')

# 7) Найти индекс ряда с минимальной суммой элементов.
line_index_min_sum = sum_elements_in_line.index(min(sum_elements_in_line))
print(f'Индекс ряда с минимальной суммой элементов - {line_index_min_sum}')

# 6) Найти индекс колонки с максимальной суммой элементов.
# 8) Найти индекс колонки с минимальной суммой элементов.
i = 0
sum_elements_in_column = []
while i < n:
    one_column_sum = 0
    for line in random_matrix:
        one_column_sum += line[i]
    sum_elements_in_column.append(one_column_sum)
    i += 1
column_index_max_sum = sum_elements_in_column.index(max(sum_elements_in_column))
print(f'Индекс колонки с максимальной суммой элементов - {column_index_max_sum}')

column_index_min_sum = sum_elements_in_column.index(min(sum_elements_in_column))
print(f'Индекс колонки с минимальной суммой элементов - {column_index_min_sum}')

# 9) Обнулить все элементы выше главной диагонали.
matrix_0_above = []
i = 0
for line in random_matrix:
    new_line = []
    j = 0
    for element in line:
        if j <= i:
            new_line.append(element)
        else:
            new_line.append(0)
        j += 1
    matrix_0_above.append(new_line)
    i += 1
print(f'Matrix with 0 above main diagonal:')
print_matrix(matrix_0_above)


# 10) Обнулить все элементы ниже главной диагонали.
matrix_0_below = []
i = 0
for line in random_matrix:
    new_line = []
    j = 0
    for element in line:
        if j < i:
            new_line.append(0)
        else:
            new_line.append(element)
        j += 1
    matrix_0_below.append(new_line)
    i += 1
print(f'Matrix with 0 above main diagonal:')
print_matrix(matrix_0_below)
