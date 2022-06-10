n = int(input("Ширина шоколадки (долек):"))
m = int(input("Высота шоколадки (долек):"))
k = int(input("Долек нужно отломить:"))

if k % n == 0 or k % m == 0:
    print("Yes")
else:
    print("No")
