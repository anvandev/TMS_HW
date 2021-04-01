""" Закрепить знания по работе с циклами.
Дан список. Создать новый список, сдвинутый на 1 элемент влево
Пример: 1 2 3 4 5 -> 2 3 4 5 1 """


from copy import deepcopy


list1 = [7, 5, '10', 0, -3, 23]

# without using loops
new_list2 = deepcopy(list1)
new_list2.append(new_list2[0])
del new_list2[0]
print(new_list2)


# using while loop
list2 = []
i = 1
while i < len(list1):
    list2.append(list1[i])
    i += 1
list2.append(list1[0])
print(list2)


# using for loop
list3, last_element = [], None
for i, element in enumerate(deepcopy(list1)):
    if i:
        list3.append(element)
    else:
        last_element = element
list3.append(last_element)
print(list3)

# using for loop (old)
list2 = []
i = 1
for element in list1:
    if i < len(list1):
        list2.append(list1[i])
        i += 1
    else:
        list2.append(list1[0])
print(list2)
