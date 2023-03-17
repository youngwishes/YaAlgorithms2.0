d = int(input())
x0, y0 = list(map(int, input().split()))

A = (0, 0)
B = (d, 0)
C = (0, d)


x1, y1 = A
x2, y2 = B
x3, y3 = C

C0 = (x0 - x1) * (y3 - y2) - (x3 - x1) * (y0 - y1)
B0 = (x0 - x2) * (y1 - y2) - (x1 - x2) * (y0 - y2)
A0 = (x0 - x3) * (y2 - y3) - (x2 - x3) * (y0 - y3)

# - Если D = 0 - значит, точка С лежит на прямой АБ.
# - Если D < 0 - значит, точка С лежит слева от прямой.
# - Если D > 0 - значит, точка С лежит справа от прямой.

if A0 >= 0 and B0 >= 0 and C0 >= 0:
    print(0)
else:
    A = (x0 - x1) ** 2 + (y0 - y1) ** 2
    B = (x0 - x2) ** 2 + (y0 - y2) ** 2
    C = (x0 - x3) ** 2 + (y0 - y3) ** 2

    points_l = [A, B, C]
    min_val = min(points_l)

    dct = {A: 1, B: 2, C: 3}

    if points_l.count(min_val) > 1:
        if A == B:
            print(1)
        elif A == C:
            print(1)
        elif B == C:
            print(2)
    else:
        print(dct.get(min_val))

