n = int(input())

goods = []

for _ in range(n):
    l, r = map(int, input().split())
    goods.append((l, 1))
    goods.append((l + r, -1))

goods.sort()
count = 0
max_duration = 0
for t, event in goods:
    if event == 1:
        count += 1
    else:
        count -= 1
    if count > max_duration:
        max_duration = count

print(max_duration)
