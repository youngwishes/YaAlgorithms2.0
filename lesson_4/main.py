# Сортировка подсчетом

def countsort(seq):
    minval = min(seq)
    maxval = max(seq)

    k = (maxval - minval + 1)
    count = [0] * k

    for now in seq:
        count[now - minval] += 1

    nowpos = 0
    for val in range(k):
        for i in range(count[val]):
            seq[nowpos] = val + minval
            nowpos += 1
    print(seq)

countsort([2, 4, 1, 9, 2, 3, 4, 5, 5])
