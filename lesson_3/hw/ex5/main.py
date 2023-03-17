witnesses_count = int(input())
indications_list = []

for witness in range(witnesses_count):
    indications = set(input())
    indications_list.append(indications)

numbers_count = int(input())
witness_count = -1

suspected_numbers = []
suspect = ''

for number in range(numbers_count):
    auto_number = input()
    counter = 0
    for i_set in indications_list:
        if i_set.issubset(auto_number):
            counter += 1

    if counter > witness_count:
        witness_count = counter
        suspect = auto_number
    elif counter == witness_count:
        if suspect not in suspected_numbers:
            suspected_numbers.append(suspect)
        suspected_numbers.append(auto_number)

if suspected_numbers:
    print('\n'.join(suspected_numbers))
else:
    print(suspect)
