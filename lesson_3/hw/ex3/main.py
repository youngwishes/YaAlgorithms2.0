numbers = list(map(int, input().split()))

for i, num in enumerate(numbers):
    if numbers.count(num) == 1:
        print(num)
