from utilities import read_file

def day3_part1(is_test: bool=True):
    if is_test:
        file = "data/day3_sample.txt"
    else:
        file = "data/day3.txt"
    
    grid = read_file(file)

    close_vals = []
    for row_index, line in enumerate(grid):
        current_ints = []

        current_num = False
        symbol_adjacent = False
        for col_index, char in enumerate(line):

            # end of one number
            if char == '.' and current_num:

                # last symbol check
                if not symbol_adjacent:
                    symbol_adjacent = check_up_down(grid, row_index, col_index)

                if symbol_adjacent:
                    close_vals.append(int(''.join(current_ints)))

                current_num = False
                symbol_adjacent = False
                current_ints = []
            
            # skip repeated '.'
            elif char == '.':
                continue
            
            # another number
            elif char.isnumeric():
                current_ints.append(char)

                # first number in the series
                if not current_num:
                    # check left corners
                    symbol_adjacent = check_up_down(grid, row_index, col_index - 1)

                    try: # check left side
                        symbol_adjacent = symbol_adjacent or \
                            grid[row_index][col_index - 1] != '.' and not grid[row_index][col_index - 1].isnumeric()
                    except:
                        pass

                # check up / down
                symbol_adjacent = symbol_adjacent or check_up_down(grid, row_index, col_index)

                current_num = True

                # end of the line
                if col_index == len(line) - 1:
                    if symbol_adjacent:
                        close_vals.append(int(''.join(current_ints)))
                    current_num = False
                    symbol_adjacent = False
                    current_ints = []

            # special symbol on the line
            elif char not in '0123456789.' and current_num:
                close_vals.append(int(''.join(current_ints)))

                current_num = False
                symbol_adjacent = False
                current_ints = []

    return sum(close_vals)

def check_up_down(grid, row_index, col_index):
    symbol_adjacent = False
    try:
        symbol_adjacent = grid[row_index - 1][col_index] != '.' and not grid[row_index - 1][col_index].isnumeric()
    except:
        pass
    try:
        symbol_adjacent = symbol_adjacent or \
            grid[row_index + 1][col_index] != '.' and not grid[row_index + 1][col_index].isnumeric()
    except:
        pass
    return symbol_adjacent



def day3_part2(is_test: bool=True):
    if is_test:
        file = "data/day3_sample.txt"
    else:
        file = "data/day3.txt"

    grid = read_file(file)
    close_vals = []
    gears = []
    for row_index, line in enumerate(grid):
        current_ints = []

        current_num = False
        symbol_adjacent = False
        for col_index, char in enumerate(line):
            # add gear information
            if char not in '0123456789.':
                gears.append([row_index, col_index, 0])

            # end of one number
            if char == '.' and current_num:

                # last symbol check
                if not symbol_adjacent:
                    symbol_adjacent = check_up_down(grid, row_index, col_index)

                if symbol_adjacent:
                    close_vals.append((row_index, col_index - 1, int(''.join(current_ints))))

                current_num = False
                symbol_adjacent = False
                current_ints = []
            
            # skip repeated '.'
            elif char == '.':
                continue
            
            # another number
            elif char.isnumeric():
                current_ints.append(char)

                # first number in the series
                if not current_num:
                    # check left corners
                    symbol_adjacent = check_up_down(grid, row_index, col_index - 1)

                    try: # check left side
                        symbol_adjacent = symbol_adjacent or \
                            grid[row_index][col_index - 1] != '.' and not grid[row_index][col_index - 1].isnumeric()
                    except:
                        pass

                # check up / down
                symbol_adjacent = symbol_adjacent or check_up_down(grid, row_index, col_index)

                current_num = True

                # end of the line
                if col_index == len(line) - 1:
                    if symbol_adjacent:
                        close_vals.append((row_index, col_index, int(''.join(current_ints))))
                    current_num = False
                    symbol_adjacent = False
                    current_ints = []

            # special symbol on the line
            elif char not in '0123456789.' and current_num:
                close_vals.append((row_index, col_index - 1, int(''.join(current_ints))))

                current_num = False
                symbol_adjacent = False
                current_ints = []

    close_vals.sort()

    return calculate_gears(gears, grid, close_vals)

def calculate_gears(gears, grid, close_vals):
    for index, (row, col, _) in enumerate(gears):
        pair = []
        # x is the right-most character
        for y, x, value in close_vals:
            if y - 1 <= row <= y + 1 \
                and (x == col - 1 or x == col or (x > col and x <= col + len(str(value)))):
                    pair.append(value)
        if len(pair) == 2:
            gears[index][2] = pair[0] * pair[1]
    
    return sum(gear[2] for gear in gears)




print(day3_part2(False))