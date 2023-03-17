input_data = [2, 2, 2, 5, 2, 3, 6, 9, 3, 1, 3, 4, 6]


def check_water_cells(land):
    max_column_index = 0

    for index in range(len(land)):
        if land[index] > land[max_column_index]:
            max_column_index = index

    max_left_column_index = 0
    left_water_cells = 0

    for index in range(max_column_index):
        if land[index] > land[max_left_column_index]:
            max_left_column_index = index

        left_water_cells += land[max_left_column_index] - land[index]

    max_right_column_index = 0
    right_water_cells = 0

    for index in range(len(land) - 1, max_column_index, -1):
        if land[index] > land[max_right_column_index]:
            max_right_column_index = index

        right_water_cells += land[max_right_column_index] - land[index]

    return left_water_cells + right_water_cells


result = check_water_cells(input_data)
print(result)
