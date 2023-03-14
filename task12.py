'''Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

*Пример:*

A = 3; B = 5 -> 243 (3⁵)
    A = 2; B = 3 -> 8 '''

number = int(input("Введите число: "))
exp = int(input("Введите степень: "))

def result(number, exp):
    if (exp == 1):
        return (number)
    if (exp != 1):
        return (number * result(number, exp - 1)) # умножаем число на себя в меньшей на 1 степени - во имя рекурсии
    if (exp == 0):
        return 1

print(f'При возведении числа {number} в степень {exp} получим {result(number, exp)}')