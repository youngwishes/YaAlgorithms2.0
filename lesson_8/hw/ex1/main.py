class Node:
    def __init__(self, value=None):
        self.left = None
        self.right = None
        self.value = value


def add(root, value):
    if root.value == value:
        result = "ALREADY"
    elif root.value > value:
        if root.left:
            result = add(root.left, value)
        else:
            root.left = Node(value=value)
            root.left.parent = root
            result = "DONE"
    else:
        if root.right:
            result = add(root.right, value)
        else:
            root.right = Node(value=value)
            root.right.parent = root
            result = "DONE"

    return result


def search(root, value):
    if root:
        if root.value == value:
            result = "YES"
        elif root.value > value:
            if root.left:
                result = search(root.left, value)
            else:
                result = "NO"
        else:
            if root.right:
                result = search(root.right, value)
            else:
                result = "NO"
    else:
        result = "NO"

    return result


def printtree(root, depth=0):
    if root is None:
        return

    printtree(root.left, depth + 1)
    print(f'{depth * "."}{root.value}')
    printtree(root.right, depth + 1)


with open('input.txt', 'r') as f:
    tree = None
    for l in f:
        command, n = l.split() if len(l.split()) > 1 else (l, None)
        if command == "ADD":
            if not tree:
                tree = Node(value=int(n))
                print("DONE")
            else:
                print(add(tree, int(n)))
        elif command == "SEARCH":
            print(search(tree, int(n)))
        else:
            printtree(tree)



