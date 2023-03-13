# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть

import random

count = int(input('Сколько монеток лежит на столе?'))
coins = [random.randint(0,1) for i in range(count)]
print(coins)

if coins.count(0)>coins.count(1):
    print(f'Нужно перевернуть {coins.count(1)} решки')
else:
    print(f'Нужно перевернуть {coins.count(0)} орла(ов)')


