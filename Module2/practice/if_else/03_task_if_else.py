# Дан треугольник со сторонами a, b и c. Определите, является ли он равнобедренным.
# Формат входных данных: дано три натуральных числа. Гарантируется, что отрезки с данными длинами образуют треугольник.
# Формат выходных данных: Выведите «YES», если треугольник равнобедренный, и «NO» в противном случае.

# TODO: your code here
side1_triangle= float(input("Сторона 1:"))
side2_triangle= float(input("Сторона 2:"))
side3_triangle= float(input("Сторона 3:"))

if side1_triangle==side2_triangle or side1_triangle==side3_triangle or side2_triangle==side3_triangle:
    print("Yes")
else:
    print("No")
