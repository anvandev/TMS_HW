""" Закрепить знания по работе с lambda функциями, генераторами списков и словарей,
декораторами.
Дан список строк. Отформатировать все строки в формате ‘{i} - {string}’, где i
это порядковый номер строки в списке. Использовать генератор списков. """

universe = ['galaxy', 'moon', 'earth']

universe_index = [f'{i+1} - {element}' for i, element in enumerate(universe)]
print(universe_index)
