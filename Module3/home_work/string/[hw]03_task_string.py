# Посчитайте количество согласных букв в данной строке.

text = input("Введите текст:")
consonants = "бвгдзклмнпрстфхцчщ"
text_low = text.lower()

total_consonants = 0
i = 0  # индекс нужной буквы

for _ in consonants:
    counting = text_low.count(consonants[i])
    total_consonants += counting
    i += 1

print(f"{total_consonants} согласных букв в тексте")
