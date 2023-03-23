# Левый бинарный поиск

def leftbinarysearch(seq, l, r, x):
    while (r - l) > 1:
        m = (l + r) // 2

        if seq[m] <= x:
            l = m
        else:
            r = m

    return l


# Правый бинарный поиск (минимальный элемент, который >= икса)
def rightbinarysearch(seq, l, r, x):
    while (r - l) > 1:
        m = (l + r) // 2

        if seq[m] >= x:
            r = m
        else:
            l = m

    return r


#
# for i in range(0, 6):
#     print(leftbinarysearch([1, 2, 3, 4], -1, 4, i))
seq = [1, 2, 2, 2, 5, 8, 13, 21, 27, 35, 35, 35, 35]
min_elem_more_than_x = rightbinarysearch(seq, -1, len(seq), 35)

print(min_elem_more_than_x)
#

max_elem_less_than_x = leftbinarysearch(seq, -1, len(seq), 21)
print(max_elem_less_than_x)
#
# min_elem_more_than_x = rightbinarysearch(seq, -1, len(seq), 3)
#
# print(seq[min_elem_more_than_x])
#
# max_elem_less_than_x = leftbinarysearch(seq, -1, len(seq), 3)
# print(seq[max_elem_less_than_x])
