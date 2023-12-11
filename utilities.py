def read_file(input_file: str, strip: bool = True) -> list[str]:
    result = []
    with open(input_file) as in_file:
        for line in in_file:
            if strip:
                line = line.strip()
            result.append(line)

    return result

def get_lines(day: int, is_test: bool, strip: bool = True) -> list[str]:
    if is_test:
        file = f"data/day{day}_sample.txt"
    else:
        file = f"data/day{day}.txt"

    return read_file(file, strip)

def print_grid(grid: list[list]):
    for row in grid:
        for val in row:
            print(val, end='')
        print()