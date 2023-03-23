def y(a, b, c, d, x):
    return a * x ** 3 + b * x ** 2 + c * x + d


def left_binsearch(a, b, c, d):
    lx = -10 ** 9
    rx = 10 ** 9
    if a > 0:
        while rx - lx > 1e-5:
            x = (lx + rx) / 2
            res = y(a, b, c, d, x=x)
            if res > 0:
                rx = x
            else:
                lx = x
    else:
        while rx - lx > 1e-5:
            x = (lx + rx) / 2
            res = y(a, b, c, d, x=x)
            if res > 0:
                lx = x
            else:
                rx = x
    return lx


with open('cubroot.in', 'r') as f:
    for i_line in f:
        a, b, c, d = map(int, i_line.split())
        print(left_binsearch(a, b, c, d))
