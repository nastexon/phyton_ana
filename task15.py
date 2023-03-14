# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import random

my_list = [random.randint(-10, 10) for i in range(20)]
print(my_list)

min_predel = int(input('Введите нижнюю границу диапазона: '))
max_predel = int(input('Введите верхнюю границу диапазона: '))

print('Индексы элементов в этом диапазоне: ')
for i in range(len(my_list)):
    if min_predel <= my_list[i] <= max_predel:
        print(i, end = ", ")

