number = int(input())

max_number = number
count = 1

while number != 0:
    number = int(input())
    if number == max_number:
        max_number = number
        count += 1
    elif number > max_number:
        max_number = number
        count = 1


print(count)
