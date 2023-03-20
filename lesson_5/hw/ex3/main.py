groups_count, classrooms_count = map(int, input().split())

groups = sorted([(g, i) for i, g in enumerate(list(map(lambda x: int(x) + 1, input().split())))])
classrooms = sorted([(c, i + 1) for i, c in enumerate(list(map(int, input().split())))])

gr = 0
count = 0
groups_in_aud = [0] * groups_count

for cls, i in classrooms:
    if groups[gr][0] <= cls:
        groups_in_aud[groups[gr][1]] = i
        count += 1
        gr += 1

print(count)
print(*groups_in_aud)
