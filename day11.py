from utilities import get_lines, print_grid

def convert_grid(grid: list[str]):
    result = []
    for row in grid:
        result.append(list(row))
    return result

def get_empty_cols(grid: list[list[str]]) -> list[int]:
    empty_cols = []
    for col_index in range(len(grid[0])):
        checks = [grid[row_index][col_index] == '.' for row_index in range(len(grid))]
        empty = all(checks)
        if empty:
            empty_cols.append(col_index)
    return empty_cols

def expand_cols(grid: list[list[str]], to_expand: list[int], factor: int = 1):
    to_expand = sorted(to_expand, reverse=True)

    for new_col in to_expand:
        for row_index in range(len(grid)):
            for _ in range(factor):
                grid[row_index].insert(new_col, '.')

def get_empty_rows(grid: list[list[str]]) -> list[int]:
    empty_rows = []
    for row_index in range(len(grid)):
        empty = all([grid[row_index][col_index] == '.' for col_index in range(len(grid[row_index]))])
        if empty:
            empty_rows.append(row_index)
    return empty_rows

def expand_rows(grid: list[list[str]], to_expand: list[int], factor: int = 1):
    to_expand = sorted(to_expand, reverse=True)

    for new_row in to_expand:
        row = ['.'] * len(grid[0])
        for _ in range(factor):
            grid.insert(new_row, row)

def find_hashtag(grid: list[list[str]]):
    stars = []
    for row_index in range(len(grid)):
        for col_index in range(len(grid[row_index])):
            if grid[row_index][col_index] == '#':
                stars.append((row_index, col_index))
    return stars


def taxi_cab_distance(point_one: tuple[int, int], point_two: tuple[int, int]):
    return abs(point_two[1] - point_one[1]) + abs(point_two[0] - point_one[0])

def part1(is_test: bool = True):
    all_lines = get_lines(11, is_test)
    all_lines = convert_grid(all_lines)
    empty_cols = get_empty_cols(all_lines)
    empty_rows = get_empty_rows(all_lines)

    expand_cols(all_lines, empty_cols)
    expand_rows(all_lines, empty_rows)

    stars = find_hashtag(all_lines)

    distance_map = []
    for _ in range(len(stars)):
        distance_map.append([0] * len(stars))

    for index, coord_one in enumerate(stars):
        for index2, coord_two in enumerate(stars):
            # we just need to create the upper diagonal
            if index == index2 or index2 < index:
                continue
            
            distance_map[index][index2] = taxi_cab_distance(coord_one, coord_two)

    #print_grid(distance_map)
    return sum([sum(row) for row in distance_map])


# print(part1(False))

def find_crossings(star_one: tuple[int, int], star_two: tuple[int, int], empty_cols: list[int], empty_rows: list[int]):
    crossings = 0
    for empty_col in empty_cols:
        if star_one[1] < empty_col < star_two[1]:
            crossings += 1

        if star_two[1] < empty_col < star_one[1]:
            crossings += 1

    for empty_row in empty_rows:
        if star_one[0] < empty_row < star_two[0]:
            crossings += 1

        if star_two[0] < empty_row < star_one[0]:
            crossings += 1

    return crossings

def part2(factor: int = 999999, is_test: bool = True):
    all_lines = get_lines(11, is_test)
    all_lines = convert_grid(all_lines)
    empty_cols = get_empty_cols(all_lines)
    empty_rows = get_empty_rows(all_lines)

    # expand_cols(all_lines, empty_cols, 1000000)
    # expand_rows(all_lines, empty_rows, 1000000)

    stars = find_hashtag(all_lines)

    distance_map = []
    for _ in range(len(stars)):
        distance_map.append([0] * len(stars))

    for index, coord_one in enumerate(stars):
        for index2, coord_two in enumerate(stars):
            # we just need to create the upper diagonal
            if index == index2 or index2 < index:
                continue
            
            crossings = find_crossings(coord_one, coord_two, empty_cols, empty_rows)
            distance_map[index][index2] = taxi_cab_distance(coord_one, coord_two) + (factor - 1) * crossings


    #print_grid(distance_map)
    return sum([sum(row) for row in distance_map])

print(part2(False))