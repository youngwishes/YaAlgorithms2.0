n = int(input())
seq = list(map(int, input().split()))
m = int(input())
queries = list(map(int, input().split()))


def left_binsearch(seq, elem):
    l = -1
    r = n

    while r - l > 1:
        m = (r + l) // 2

        if seq[m] <= elem:
            l = m
        else:
            r = m

    return l


def right_binsearch(seq, elem):
    l = -1
    r = n

    while r - l > 1:
        m = (r + l) // 2

        if seq[m] >= elem:
            r = m
        else:
            l = m

    return r


for query in queries:
    last = left_binsearch(seq, elem=query)
    first = right_binsearch(seq, elem=query)
    if seq[last] != query:
        print(0, 0)
    else:
        print(first + 1, last + 1)
