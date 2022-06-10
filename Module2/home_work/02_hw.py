# По данному числу n закончите фразу «На лугу пасется...» одним из возможных продолжений:
# «n коров», «n корова», «n коровы», правильно склоняя слово «корова».
# Формат входных данных
# Дано целое положительное число n
# Формат выходных данных
# Программа должна вывести введенное число n и одно из слов (на латинице):
# коров, корова или коровы
# Например, 1 корова, 2 коровы, 5 коров, 125 коров.

cow_number = int(input("Сколько коров склонять будем?:"))

if cow_number%100 == 11 or cow_number%100 == 12 or cow_number%100 == 13 or cow_number%100 == 14 :
    print(cow_number, "krorov")
elif cow_number % 10 == 1:
    print(cow_number, "krorova")
elif cow_number % 10 == 2 or cow_number % 10 == 3 or cow_number % 10 == 4:
    print(cow_number, "krorovy")
else:
    print(cow_number, "krorov")
