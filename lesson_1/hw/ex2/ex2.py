input_data = input().split()

n, i, j = list(map(int, input_data))
result = 0

diff = abs(j - i)

if diff <= n // 2:
    result = diff - 1
else:
    result = n - diff - 1

print(result)
