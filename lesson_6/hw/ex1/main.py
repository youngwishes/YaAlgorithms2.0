n = int(input())
seq = sorted(list(map(int, input().split())))
k = int(input())

for i in range(k):
    x1, x2 = map(int, input().split())

    l = -1
    r = n

    while r - l > 1:
        m = (r + l) // 2
        if seq[m] >= x1:
            r = m
        else:
            l = m

    l = -1
    r1 = n

    while r1 - l > 1:
        m = (r1 + l) // 2
        if seq[m] <= x2:
            l = m
        else:
            r1 = m

    if r <= l:
        print(len(seq[r: l]) + 1, end=' ')
    else:
        print(0, end=' ')
