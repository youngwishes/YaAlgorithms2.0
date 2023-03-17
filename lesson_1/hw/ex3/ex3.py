x, y, z = list(map(int, input().split()))

result = 0
if x > 12 or y > 12:
    result = 1
elif x == y:
    result = 1

print(result)
