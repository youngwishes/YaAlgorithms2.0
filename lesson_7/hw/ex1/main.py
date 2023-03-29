n = int(input())

summa = 0
lrs_list = []

for _ in range(n):
    l, r = map(int, input().split())
    lrs_list.append((l, r))

lrs_list.sort()
last_start = -10 ** 9
for elem in lrs_list:
    if elem[0] < last_start:
        if elem[1] > last_start:
            summa += elem[1] - last_start
            last_start = elem[1]
    else:
        summa += elem[1] - elem[0]
        last_start = elem[1]

print(summa)
