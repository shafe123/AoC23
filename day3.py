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
        end_of_num = False
        symbol_adjacent = False
        for col_index, char in enumerate(line):

            # end of one number
            if char == '.' and current_num or col_index == len(line) - 1:
                end_of_num = True

                # last symbol check
                if not symbol_adjacent:
                    symbol_adjacent = check_up_down(grid, row_index, col_index)

                if symbol_adjacent:
                    close_vals.append(int(''.join(current_ints)))

                current_num = False
                end_of_num = False
                symbol_adjacent = False
                current_ints = []
            
            elif char == '.':
                continue
                
            elif char.isnumeric():
                current_ints.append(char)

                if not current_num:
                    # check left side
                    symbol_adjacent = check_up_down(grid, row_index, col_index - 1)

                    try: # check to the left
                        symbol_adjacent = symbol_adjacent or \
                            grid[row_index][col_index - 1] != '.' and not grid[row_index][col_index - 1].isnumeric()
                    except:
                        pass

                current_num = True

                if not symbol_adjacent:
                    symbol_adjacent = check_up_down(grid, row_index, col_index)
            
            elif current_num:
                close_vals.append(int(''.join(current_ints)))

                current_num = False
                end_of_num = False
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


print(day3_part1(False))