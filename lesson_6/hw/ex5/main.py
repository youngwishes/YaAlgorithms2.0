n, k = map(int, input().split())
seq = sorted(list(map(int, input().split())))

left = 0
right = seq[-1] - seq[0]


def is_good(seq, l):
    count = 0
    last = seq[0] - 1
    for elem in seq:
        if elem > last:
            count += 1
            last = elem + l
    return count


while left < right:
    l = (left + right) // 2
    if is_good(seq, l) > k:
        left = l + 1
    else:
        right = l

print(left)
