words = {}

with open('input.txt', 'r') as f:
    for l in f.readlines():
        line = l.split()

        for word in line:
            words[word] = words.get(word, 0) + 1

    swapped_dict = {}

    for word, index in words.items():
        if index not in swapped_dict:
            swapped_dict[index] = [word]
        else:
            swapped_dict[index].append(word)

    for key in sorted(swapped_dict, reverse=True):
        words = sorted(swapped_dict.get(key))

        print('\n'.join(words))
