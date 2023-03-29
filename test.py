n, m = map(int, input().split())
points = list(map(int, input().split()))

for i in range(len(points)):
    points[i] = (points[i], 0)
result = []

for i in range(m):
    l, r = map(int, input().split())
    points.append((l, -1, i))
    points.append((r, 1, i))

points.sort()

segmentsdct = {}
pointsdct = {}
startcount = 0
last_startcount = 0
last_start = -1
for p in points:
    if p[1] == -1:
        if last_start != p[0]:
            startcount += 1
        segmentsdct[p[2]] = startcount
        last_start = p[0]
    elif p[1] == 0:
        if not pointsdct.get(startcount):
            pointsdct[startcount] = pointsdct.get(startcount - 1, 0) + 1
        else:
            pointsdct[startcount] += 1
        last_startcount = startcount
    else:
        totalpoints = pointsdct.get(last_startcount, 0) - pointsdct.get(segmentsdct[p[2]] - 1, 0)
        result.append((p[2], totalpoints))




for ans in sorted(result):
    print(ans[1])