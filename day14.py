from utilities import get_lines, grid_string


def percolate_up(grid, row_index, col_index):
    for upper_row in range(row_index - 1, -1, -1):
        if grid[upper_row][col_index] == '.':
            grid[upper_row][col_index] = 'O'
            grid[upper_row + 1][col_index] = '.'
        else:
            break
    return grid


def part1(is_test: bool = True):
    all_lines = get_lines(14, is_test)

    for index in range(len(all_lines)):
        all_lines[index] = list(all_lines[index])

    for row_index, row in enumerate(all_lines):
        for col_index, val in enumerate(row):
            if val == 'O':
                percolate_up(all_lines, row_index, col_index)

    return total_load(all_lines)

def total_load(all_lines):
    loads = []
    for row_index, row in enumerate(all_lines[::-1]):
        multiplier = row_index + 1
        rocks = row.count('O')
        loads.append(multiplier * rocks)

    return sum(loads)

# print(part1(False))


def rotate_list(grid):
    new_list = list(map(list, zip(*grid[::-1])))
    return new_list

import copy
def part2(is_test: bool = True):
    all_lines = get_lines(14, is_test)

    for index in range(len(all_lines)):
        all_lines[index] = list(all_lines[index])

    cache = {}
    all_grids = []
    for x in range(1000000):
        for _ in range(4):
            for row_index, row in enumerate(all_lines):
                for col_index, val in enumerate(row):
                    if val == 'O':
                        all_lines = percolate_up(all_lines, row_index, col_index)
            all_lines = rotate_list(all_lines)
        
        # detect cycles
        flattened = grid_string(all_lines)
        all_grids.append(copy.deepcopy(all_lines))
        if flattened in cache:
            cycle_length = x - cache[flattened]
            final_index = cache[flattened] + (1000000000 - cache[flattened]) % cycle_length
            return total_load(all_grids[final_index - 1])

        cache[flattened] = x
        

print(part2(False))