""" Закрепить знания по работе с циклами и условиями.
В заданной строке расположить в обратном порядке все слова. Разделителями
слов считаются пробелы. """

s = 'межгалактический полет может затянуться'

# without using loop
s2_list = s.split()[::-1]
s_yoda_style = ' '.join(s2_list)
print(s_yoda_style)


# # using for loop in list comprehension
# s3_list = s.split()
# s_list_reversed = [word for word in s3_list[::-1]]
# s_yoda_style = ' '.join(s_list_reversed)
# print(s_yoda_style)
