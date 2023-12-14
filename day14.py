from utilities import get_lines, print_grid


def percolate_up(grid, row_index, col_index):
    for upper_row in range(row_index - 1, -1, -1):
        if grid[upper_row][col_index] == '.':
            grid[upper_row][col_index] = 'O'
            grid[upper_row + 1][col_index] = '.'
        else:
            break


def part1(is_test: bool = True):
    all_lines = get_lines(14, is_test)

    for index in range(len(all_lines)):
        all_lines[index] = list(all_lines[index])

    for row_index, row in enumerate(all_lines):
        for col_index, val in enumerate(row):
            if val == 'O':
                percolate_up(all_lines, row_index, col_index)

    loads = []
    for row_index, row in enumerate(all_lines[::-1]):
        multiplier = row_index + 1
        rocks = row.count('O')
        loads.append(multiplier * rocks)

    return sum(loads)

    

print(part1(False))