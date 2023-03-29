# not solved
from math import pi

n = int(input())
fs = []
max_r1 = 10 ** 6
min_r2 = 0

for i in range(1, n + 1):
    r1, r2, f1, f2 = map(float, input().split())
    max_r1 = max(max_r1, r1)
    min_r2 = min(min_r2, r2)
    fs.append((f1, -i))
    fs.append((f2, i))

fs.sort()

sqrscount = 0
sqrs = set()

for f in fs:
    if f[1] < 0:
        sqrs.add(-f[1])
        sqrscount += 1
    elif f[1] in sqrs:
        sqrscount -= 1
# s = 0.5 * (f2 - f1) * r ** 2
summa = 0
for i in range(len(fs)):
    event = fs[i]

    if event[1] < 0:
        sqrscount += 1
    else:
        sqrscount -= 1

    if sqrscount > 1:
        if i < len(fs) - 1:
            summa += (fs[i + 1][0] - fs[i][0]) * (max_r1 ** 2 - min_r2 ** 2) / 2
        else:
            summa += (fs[0][0] - fs[len(fs) - 1][0] + 2 * pi) * (max_r1 ** 2 - min_r2 ** 2) / 2

print(summa)
