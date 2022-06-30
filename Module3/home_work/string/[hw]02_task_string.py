# Дана строка состоящая из слов, все слова разделены ровно одним пробелом. Знаки препинания отсутствуют.
# Найдите первое слово, начинающееся на букву "б"
# если слова на эту букву нет, выведите "слов на б нет"
text = input("Введите текст:")

format_text = text.lower().split()
words_with_b = []
count_b = 0
for word in format_text:
    b_word = word.startswith("б")
    if b_word == True:
        words_with_b.append(word)
        count_b += 1
if count_b > 0:
    print(f"Первое слово на <<Б>>: {words_with_b[0]}. Всего слов на <<Б>>: {count_b}")
else:
    print("слов на <<Б>> нет")
