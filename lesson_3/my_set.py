setsize = 10
myset = [[] for _ in range(setsize)]


def add(x):
    if not find(x):
        myset[x % setsize].append(x)


def find(x):
    for now in myset[x % setsize]:
        if now == x:
            return True
    return False


def delete(x):
    xlist = myset[x % setsize]
    for i in range(len(xlist)):
        if xlist[i] == x:
            xlist[i] = xlist[-1]
            xlist.pop()
            return True

# F(x) = X % setsize - хэш-функция
# myset (список списков) - хэш таблица
# Совпадение значений хэш-функции для разных параметров - коллизия
# (17 % 10 = 7, 27 % 10 = 7, 17 и 27 - параметры, 7 - результат работы хэш-функции)
