tree = {}
pairs = []

with open('input.txt', 'r') as f:
    n = int(f.readline())
    for l in f.readlines():
        child, parent = l.split()
        if n > 1:
            if not tree.get(parent):
                tree[parent] = [child]
            else:
                tree[parent].append(child)
            n -= 1
        else:
            pairs.append((child, parent))


def search_1(tree, first, second):
    childs = tree.get(first, ())

    result = 0

    if second in childs:
        return 1

    for child in childs:
        result = search_1(tree, child, second)
        if result:
            return result

    return result


def search_2(tree, first, second):
    childs = tree.get(second, ())

    result = 0

    if first in childs:
        return 2

    for child in childs:
        result = search_2(tree, first, child)
        if result:
            return result

    return result


for first, second in pairs:
    if search_1(tree, first, second):
        print(1, end=' ')
    elif search_2(tree, first, second):
        print(2, end=' ')
    else:
        print(0, end=' ')
