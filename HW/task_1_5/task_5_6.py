""" Закрепить знания по работе с циклами и условиями.
Задан целочисленный массив. Определить количество участков массива,
на котором элементы монотонно возрастают (каждое следующее число больше предыдущего). """


from array import array


numbers = array('i', [3, 2, 1, 3, 4, 5, 2, 3, 8, 5, 2, 7, 8])
number_of_sequences = 0

i = 0
while i < len(numbers) - 1:
    if numbers[i] < numbers[i+1]:
        number_of_sequences += 1
        while i < len(numbers) - 1 and numbers[i] < numbers[i+1]:
            i += 1
    i += 1
print(f'Number of sequences: {number_of_sequences}')
