# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

''' эталонное решение???
x = int(input())
y = int(input())
for i in range(x):
    for j in range(y):
        if x == i + j and y == i * j:
            print(i, j) '''

import math

# Нужно решить систему уравнений:
# summ = x + y
# proizv = x * y

# x = summ - y
# p = (s - y) * y

# y*y - s * y + p = 0

summ = s = int(input('Сумма двух натуральных чисел Х и У: '))
proizv = p = int(input('Произведение двух натуральных чисел Х и У: '))

discremenant = s*s -4*p
if discremenant > 0:
    y1 = (s + discremenant**0.5)/2
    y2 = (s - discremenant**0.5)/2
    x1 = summ - y1
    x2 = summ - y2
    print(int(x1), int(y1))
    print(int(x2), int(y2))
elif discremenant == 0:
    y = s/2
    x = summ - y
    print(int(x), int(y))
else:
    print("Петя сказал неправду")





