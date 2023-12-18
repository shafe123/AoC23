from utilities import get_lines


def find_S(grid: list[list[str]]) -> tuple[int, int]:
    for row_index, row in enumerate(grid):
        for col_index, value in enumerate(row):
            if value == "S":
                return row_index, col_index


def get_neighbors(
    grid: list[list[str]], point: tuple[int, int]
) -> list[tuple[int, int]]:
    row, col = point

    neighbors = []
    piece = grid[row][col]
    if piece == "|":
        neighbors.append((row - 1, col))
        neighbors.append((row + 1, col))
    elif piece == "-":
        neighbors.append((row, col - 1))
        neighbors.append((row, col + 1))
    elif piece == "L":
        neighbors.append((row - 1, col))
        neighbors.append((row, col + 1))
    elif piece == "7":
        neighbors.append((row, col - 1))
        neighbors.append((row + 1, col))
    elif piece == "F":
        neighbors.append((row, col + 1))
        neighbors.append((row + 1, col))
    elif piece == "J":
        neighbors.append((row, col - 1))
        neighbors.append((row - 1, col))

    return neighbors


def part1(is_test: bool = True):
    all_lines = get_lines(10, is_test)
    start = find_S(all_lines)

    # get initial neighbors
    return get_main_loop(all_lines, start)


def get_main_loop(all_lines, start):
    to_check = []
    for row_diff in range(-1, 2):
        for col_diff in range(-1, 2):
            row = start[0] + row_diff
            col = start[1] + col_diff
            if (
                row < 0
                or col < 0
                or row >= len(all_lines)
                or col >= len(all_lines[0])
                or row == col
            ):
                continue
            start_neighbors = get_neighbors(all_lines, (row, col))
            if start in start_neighbors:
                to_check.append((row, col))

    count = 0
    visited = [start]
    while to_check:
        next_val = to_check.pop(0)
        neighbors = get_neighbors(all_lines, next_val)

        if len(neighbors) != 2:
            print("error in neighbors...")

        i = 0
        while i < len(neighbors):
            if neighbors[i] in visited:
                neighbors.pop(i)
            else:
                i += 1

        if neighbors:
            to_check.append(neighbors[0])
        visited.append(next_val)

    return visited


# print((len(part1(False)) - 1) / 2)


def print_grid(grid: list[list[str]]):
    conversion = {
        "7": "┓",
        "L": "┗",
        "F": "┏",
        "J": "┛",
        "|": "┃",
        "-": "━",
        ".": "o",
        "S": "X",
        "*": "*"
    }
    for row in grid:
        for col in row:
            print(conversion[col], end="")
        print()


import copy


def expand_horizontally(grid: list[list[str]]):
    grid = copy.deepcopy(grid)
    for row_index, row in enumerate(grid):
        row = list(row)

        col_index = 0
        while col_index < len(row) - 1:
            if row[col_index + 1] in ["J", "-", "7"] and row[col_index] in [
                "-",
                "F",
                "L",
                "S",
            ]:
                row.insert(col_index + 1, "-")
            elif row[col_index + 1] == "S" and row[col_index] in ["-", "F", "L"]:
                row.insert(col_index + 1, "-")
            else:
                row.insert(col_index + 1, ".")
            col_index += 2
        grid[row_index] = row

    return grid


def expand_vertically(grid: list[list[str]]):
    grid = copy.deepcopy(grid)
    row_index = 0
    # create an empty new row
    while row_index < len(grid) - 1:
        new_row = ["."] * len(grid[row_index])

        for col_index in range(len(grid[row_index])):
            if grid[row_index + 1][col_index] in ["|", "J", "L", "S"] and grid[
                row_index
            ][col_index] in ["|", "F", "7"]:
                new_row[col_index] = "|"
            elif grid[row_index][col_index] == "S" and grid[row_index + 1][
                col_index
            ] in ["|", "J", "L"]:
                new_row[col_index] = "|"

        grid.insert(row_index + 1, new_row)
        row_index += 2

    return grid


def mark_escapees(grid: list[list[str]], main_loop):
    grid = copy.deepcopy(grid)
    to_visit = [(0, 0), (len(grid) - 1, len(grid[0]) - 1)]

    # if they can reach the outer edge, they can escape
    # start by adding all outer edge nodes to visit
    for col in range(1, len(grid[0])):
        to_visit.append((0, col))
        to_visit.append((len(grid) - 1, col))
    
    for row in range(1, len(grid)):
        to_visit.append((row, 0))
        to_visit.append((row, len(grid[0]) - 1))
    
    # then remove any that are already on the main loop
    index = 0
    while index < len(to_visit):
        if to_visit[index] in main_loop:
            to_visit.pop(index)
        else:
            index += 1

    visited = []

    while to_visit:
        row, col = to_visit.pop(0)
        grid[row][col] = "*"
        visited.append((row, col))
        for row_diff in range(-1, 2):
            for col_diff in range(-1, 2):
                new_point = (row + row_diff, col + col_diff)
                if (
                    new_point[0] < 0
                    or new_point[0] >= len(grid)
                    or new_point[1] < 0
                    or new_point[1] >= len(grid[0])
                    or (row_diff == 0 and col_diff == 0)
                ):
                    continue
                if (
                    new_point not in visited
                    and new_point not in to_visit
                    and new_point not in main_loop
                ):
                    to_visit.append(new_point)

    return grid


def count_offset(grid: list[list[str]], row_offset: int, col_offset: int, main_loop: list[tuple[int, int]]) -> int:
    count = 0
    for row_index in range(0, len(grid), row_offset):
        for col_index in range(0, len(grid[0]), col_offset):
            val = grid[row_index][col_index]
            if val != '*' and (row_index, col_index) not in main_loop:
                count += 1
    return count


def part2(is_test: bool = True):
    all_lines = get_lines(10, is_test)
    print_grid(all_lines)
    print("-----------------------------------")
    expanded = expand_horizontally(all_lines)
    print_grid(expanded)
    print("-----------------------------------")
    expanded = expand_vertically(expanded)
    print_grid(expanded)
    print("-----------------------------------")

    start = find_S(expanded)
    main_loop = get_main_loop(expanded, start)
    # each external square, convert them to open space
    exterior = mark_escapees(expanded, main_loop)
    print_grid(exterior)

    # determine remainder of .s
    remainders = count_offset(exterior, 2, 2, main_loop)
    print(remainders)

if __name__ == "__main__":
    part2()
