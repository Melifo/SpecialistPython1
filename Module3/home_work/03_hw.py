# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -100 до 100.
# Вывести на экран сумму всех положительных элементов кратных двум.

import random
numbers = []

n = int(input("Введите количество элементов:"))
n_total = 0
r_total = 0

while n > n_total:
    r = random.randint(-100, 100)
    print(r)
    if r > 0 and r % 2 == 0:
        r_total += r
    n_total += 1
print("Сумма всех положительных элементов кратных двум:", r_total)
