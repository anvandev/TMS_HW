""" Закрепить знания по работе с циклами и условиями.
Дана целочисленная квадратная матрица. Найти в каждой строке наи-
больший элемент и поменять его местами с элементом главной диагонали. """

from random import randint


# function to print matrix in a convenient form
def print_matrix(matrix):
    for element in matrix:
        print(element)


# create and print random matrix
n = 4
random_matrix = [[randint(1, 9) for j in range(n)] for k in range(n)]
print_matrix(random_matrix)


# find max element and swap elements

i = 0     # to count main diagonal position
for line in random_matrix:
    index_max_num = line.index(max(line))
    line[i], line[index_max_num] = line[index_max_num], line[i]
    i += 1

print('Matrix with diagonal swapped elements:')
print_matrix(random_matrix)
