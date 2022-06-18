# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -10 до 10.
# Вывести на экран сумму всех элементов.

import random

numbers = []

n = int(input("Введите количество элементов:"))
summa = 0
for _ in range(n):
    number = random.randint(-10, 10)
    numbers.append(number)
    summa += number
print(numbers)
print(summa)
