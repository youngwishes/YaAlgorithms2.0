import sys

sys.setrecursionlimit(5000)

root_tree = {}
pairs = []
with open('input.txt', 'r') as f:
    n = int(f.readline())
    flag = False
    for l in f.readlines():
        child, parent = l.split()
        if n > 1:
            root_tree[child] = parent
            n -= 1
        else:
            pairs.append((child, parent))


def get_parents_set(tree, son):
    parents = []
    parents.append(son)
    parent = tree.get(son)
    if parent:
        parents.extend(get_parents_set(tree, parent))
    return parents


for first, second in pairs:
    first = get_parents_set(root_tree, first)
    while second not in first:
        second = root_tree[second]
    print(second)