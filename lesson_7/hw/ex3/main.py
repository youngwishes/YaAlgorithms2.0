m = int(input())
segments = []

while True:
    left, right = map(int, input().split())
    if left == right == 0:
        break

    if left <= m and right >= 0:
        segments.append((left, right))

segments.sort()
bestseq = 0, 0
nowright = 0
nextright = 0
ans = []

for l, r in segments:
    if nowright < l:
        ans.append(bestseq)
        nowright = nextright
        if nowright >= m:
            break

    if nowright >= l and nextright < r:
        nextright = r
        bestseq = (l, r)

if nowright < m:
    ans.append(bestseq)

if ans[-1][1] < m:
    print('No solution')
else:
    print(len(ans))
    for l, r in ans:
        print(l, r)
