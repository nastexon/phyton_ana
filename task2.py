# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# Пример:
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

number = int(input('Сколько всего журавликов сделали ребята? '))
petr = number/6
serg = petr
kate = 2*(serg + petr)
print(f'Петя сделал {int(petr)} журавликов, Сережа сделал {int(serg)} журавликов, Катя сделала {int(kate)} журавликов,')

