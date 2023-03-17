my_set = set()

numbers = list(map(int, input().split()))

for num in numbers:
    if num not in my_set:
        print("NO")
        my_set.add(num)
    else:
        print("YES")