candidates = {}

with open('input.txt', 'r') as f:
    for l in f.readlines():
        candidate, voices = l.split()
        candidates[candidate] = candidates.get(candidate, 0) + int(voices)

    for key in sorted(candidates.keys()):
        print(key, candidates.get(key))



