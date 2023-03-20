length = int(input())
seq = list(map(int, input().split()))

summa = 0
mx = seq[0]

for num in seq:
    summa += num
    mx = max(mx, summa)
    if summa < 0:
       summa = 0

print(mx)