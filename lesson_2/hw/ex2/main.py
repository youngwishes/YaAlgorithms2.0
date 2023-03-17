houses = list(map(int, input().split()))


distances = []

for index, house in enumerate(houses):
    min_distance = 10
    if house == 1:
        for j_index, shop in enumerate(houses):
            if shop == 2:
                distance = abs(index - j_index)
                if distance < min_distance:
                    min_distance = distance

        distances.append(min_distance)

print(max(distances))

