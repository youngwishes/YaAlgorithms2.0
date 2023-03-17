max_number = int(input())

my_set = set(i for i in range(1, max_number + 1))
while True:
    ask = input()

    if ask == "HELP":
        print(*sorted(my_set))
        break
    else:
        ask = set(map(int, ask.split()))

    answer = input()

    if answer == "YES":
        my_set.intersection_update(ask)
    elif answer == "NO":
        my_set.difference_update(ask)
