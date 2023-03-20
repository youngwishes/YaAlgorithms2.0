num_to_search = int(input())

A = list(map(int, input().split()))
n1 = A[0]

B = list(map(int, input().split()))
n2 = B[0]

C = list(map(int, input().split()))
n3 = C[0]
Cs = {}

for i, val in enumerate(C[1:]):
    if val not in Cs:
        Cs[val] = i

found = None
for i in range(1, n1 + 1):
    for j in range(1, n2 + 1):
        k = Cs.get(num_to_search - A[i] - B[j])
        if k == 0 or k:
            print(i - 1, j - 1, k)
            found = True
            break
    if found:
        break
else:
    print(-1)
