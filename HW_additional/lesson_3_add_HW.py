""" урок 3. дополнительное дз  - запросить 5 имен. потом применить функцию hello ... для каждого имени """


def hello(name):
    print(f'Hello, {name}!')


names = []
i = 1
while i <= 5:
    names.append(input(f'Введите имя {i}: '))
    i += 1

for n in names:
    hello(n)
