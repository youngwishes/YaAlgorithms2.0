def left_binsearch(A, K, B, M, X):
    l = 0
    r = X

    while r - l > 1:
        m = (l + r) // 2

        if calc(A, B, K, M, m) >= X:
            r = m
        else:
            l = m
  
    return r


def calc(A, B, K, M, m):
    return (A + B) * m - ((m // K) * A + (m // M) * B)


with open('input.txt', 'r') as f:
    for i_line in f:
        A, K, B, M, X = map(int, i_line.split())
        print(left_binsearch(A, K, B, M, X))
