""" Закрепить знания по работе с циклами и условиями.
Создать список поездов. Структура словаря: номер поезда,
пункт и время прибытия, пункт и время отбытия. Вывести все сведения о поездах,
время пребывания в пути которых превышает 7 часов 20 минут. """

from datetime import datetime, timedelta


train_list = [
    {'№': 234, 'destination': 'Prague', 'arrival time': datetime(2020, 8, 11, 11, 3),
     'departure point': 'Moscow', 'departure time': datetime(2020, 8, 10, 7, 35)},
    {'№': 372, 'destination': 'Helsinki', 'arrival time': datetime(2020, 8, 14, 15, 20),
     'departure point': 'St. Petersburg', 'departure time': datetime(2020, 8, 14, 9, 15)},
    {'№': 763, 'destination': 'Berlin', 'arrival time': datetime(2020, 8, 13, 6, 20),
     'departure point': 'Kiev', 'departure time': datetime(2020, 8, 12, 18, 40)},
]

print('More then 7 hours 20 minutes:')
for train in train_list:
    if train['arrival time'] - train['departure time'] > timedelta(hours=7, minutes=20):
        travel_time = train['arrival time'] - train['departure time']
        print(f'travel time: {travel_time} --- {train}')
