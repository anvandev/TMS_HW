""" Закрепить знания по работе с циклами и условиями.
В заданной строке расположить в обратном порядке все слова. Разделителями
слов считаются пробелы. """

s = 'межгалактический полет может затянуться'

s_list = s.split()
s_list_turn = []
i = 1
for el in s_list:
    word = s_list[-i]
    s_list_turn.append(word)
    i += 1
s_yoda_style = ' '.join(s_list_turn)
print(s_yoda_style)
