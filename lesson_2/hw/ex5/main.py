folders_count = int(input())
diplomas = list(map(int, input().split()))

print(sum(diplomas) - max(diplomas))
