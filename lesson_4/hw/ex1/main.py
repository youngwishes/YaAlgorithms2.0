packages = int(input())

packages_dict = {}

for package in range(packages):
    box, color = map(int, input().split())
    packages_dict[box] = packages_dict.get(box, 0) + color

for key in sorted(packages_dict.keys()):
    print(key, packages_dict.get(key))
