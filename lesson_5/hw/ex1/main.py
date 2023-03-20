length, queries_count = map(int, input().split())
seq = list(map(int, input().split()))

prefixlist = [0 for _ in range(length + 1)]

for i in range(1, length + 1):
    prefixlist[i] = prefixlist[i - 1] + seq[i - 1]

for _ in range(queries_count):
    left, right = map(int, input().split())
    print(prefixlist[right] - prefixlist[left - 1])
