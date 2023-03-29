n, m = map(int, input().split())
points = list(map(int, input().split()))
for i in range(n):
    points[i] = (points[i], 0)

for i in range(1, m + 1):
    l, r = map(int, input().split())
    points.append((l, -i))
    points.append((r, i))

points.sort()
segmentsdct = {}
result = []
pntcount = 0

for p in points:
    if p[1] < 0:
        segmentsdct[p[1]] = pntcount
    elif p[1] == 0:
        pntcount += 1
    else:
        total_count = pntcount - segmentsdct.get(-p[1], 0)
        result.append((p[1], total_count))

for ans in sorted(result):
    print(ans[1])
