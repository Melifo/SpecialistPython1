# Дан список имен.
# Найдите самое длинное имя, если таких имен несколько - выведи любое их них

names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]

# TODO: your code here

max_len = len(names[0])
name_max = 0
for name in names:
    if len(name) > max_len:
        max_len = len(name)
        name_max = name
print(f"{name_max} - {max_len} букв")
