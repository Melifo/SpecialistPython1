## "Подсчет длинных слов"

### Задание

Даны две строки s1 и s2. Определите, можно ли составить строку s2, используя только символы из строки s1 (каждую букву можно использовать только один раз).

### Формат входных данных

Даны две строки.

### Формат выходных данных

Вывести "Да", если из символов строки s1 можно составить строку s2 и "Нет", если нельзя.

### Решение задачи

s1 = input("Введите первый текст:")
s2 = input("Введите второй текст:")

format_text_1 = s1.lower().replace(" ", "")
format_text_2 = s2.lower().replace(" ", "")
unique_letters = set(format_text_2)
count_repetitions = 0
for letter in unique_letters:
    if format_text_2.count(letter) <= format_text_1.count(letter):
        count_repetitions += 1
if count_repetitions == len(unique_letters):
    print("Да, текст возможно составить")
else:
    print("Нет, это невозможно")

