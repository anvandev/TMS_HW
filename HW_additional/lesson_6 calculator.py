# string = input(f'Input: ')

s = '23 + 3'
s_list = list(s)
print(s_list)

for i in s_list:
    if i == ' ':
        s_list.remove(i)
print(s_list)

if s_list[0].isdigit():
    s_list[0]
    print('ok')


# s_list_new = []
#
# for el in s_list:
#     if el.isdigit():
#         s_list_new.append()
#     else:
#         pass

