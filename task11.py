''' В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены
только по окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом
кусте выросло ai ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего
модуля и нескольких собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед некоторым
кустом, собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль,
находясь перед некоторым кустом заданной во входном файле грядки. '''

import random

n_bush = int(input('Сколько кустов на грядке?  '))
a_berry = [random.randint(0,10) for i in range (n_bush)] # Сколько ягодок выросло на каждом кусте на грядке
print(f'\n На грядке растет {n_bush} кустов, на каждом из них {a_berry} ягод')

summa = [sum(a_berry[:i+1]) for i in range(len(a_berry))]
print(f'\n Всего с грядки можно собрать {summa[-1]} ягод')

collect = []
for i in range (len(a_berry)-2):
    collect.append(a_berry[i]+a_berry[i+1]+a_berry[i+2])
    i = i + 1

collect.append(a_berry[-2] + a_berry[-1] + a_berry[0])
collect.append(a_berry[-1] + a_berry[0] + a_berry[1])
print(f'\n За каждый заход с трех кустов модуль собирает {collect} ягод')

max_berries = max(collect)
print(f'\n Модуль может собрать максимум {max_berries} ягод за один заход.')