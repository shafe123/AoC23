from utilities import read_file

def day3_part1(is_test: bool=True):
    if is_test:
        file = "data/day3_sample.txt"
    else:
        file = "data/day3.txt"
    
    all_lines = read_file(file)

    grid = []
    for line in all_lines:
        row = []

        for char in line:
            if char == '.':
                row.append(None)
            if char.isnumeric():
                row.append(int(char))
            else:
                row.append('x')
        grid.append(row)

    return grid_sum(grid)

def grid_sum(grid: list[list[int | str | None]]):
    sum_vals = []
    for row_index, row in enumerate(grid):
        for col_index, value in enumerate(row):
            found = False
            if value == None or value == 'x':
                continue

            for row_modifier in range(-1, 2, 1):
                for col_modifier in range(-1, 2, 1):
                    if row_modifier and col_modifier == 0:
                        continue
                    
                    try:
                        if grid[row_index + row_modifier][col_index + col_modifier] == 'x':
                            sum_vals.append(value)
                            found = True
                            break
                    except:
                        continue

                if found:
                    break
    return sum(sum_vals)



def day3_part2(is_test: bool=True):
    if is_test:
        file = "data/day3_sample.txt"
    else:
        file = "data/day3.txt"


print(day3_part1())