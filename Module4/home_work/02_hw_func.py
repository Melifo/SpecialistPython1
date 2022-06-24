# Даны координаты трех точек (xa; ya) (xb; yb) (xc; yc),
# точки соединены отрезками AB, BC и AC. Найдите отрезок с минимальной длинной.
# Если отрезков с минимальной длиной несколько - вывести любой

# При решении задачи необходимо использовать функцию расстояния между двумя точками.

def distance(x1, y1, x2, y2):
    length = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5
    return length
    pass


xa = int(input("Введите координату X точки A:"))
ya = int(input("Введите координату Y точки A:"))
xb = int(input("Введите координату X точки B:"))
yb = int(input("Введите координату Y точки B:"))
xc = int(input("Введите координату X точки C:"))
yc = int(input("Введите координату Y точки C:"))

line_ab = distance(xa, ya, xb, yb)
line_bc = distance(xb, yb, xc, yc)
line_ac = distance(xa, ya, xc, yc)

min_line = 0

if line_ac >= line_ab <= line_bc:
    min_line = "AB"
elif line_ab >= line_bc <= line_ac:
    min_line = "BC"
else:
    min_line = "AC"

print("Самый короткий отрезок:", min_line)
