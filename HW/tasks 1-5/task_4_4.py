""" Закрепить знания по работе с циклами.
Дан список. Создать новый список, сдвинутый на 1 элемент влево
Пример: 1 2 3 4 5 -> 2 3 4 5 1 """

list1 = [7, 5, '10', 0, -3, 23]

# using while loop
list2 = []
i = 1
while i < len(list1):
    list2.append(list1[i])
    i += 1
list2.append(list1[0])
print(list2)


# using for loop
list2 = []
i = 1
for element in list1:
    if i < len(list1):
        list2.append(list1[i])
        i += 1
    else:
        list2.append(list1[0])
print(list2)
