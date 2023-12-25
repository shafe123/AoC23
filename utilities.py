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

def grid_string(grid: list[list]):
    return ''.join([''.join(row) for row in grid])

def add_tuples[T](tuple_one: tuple[T, T], tuple_two: tuple[T, T]) -> tuple[T, T]:
    assert len(tuple_one) == 2 and len(tuple_two) == 2
    return tuple([one + two for one, two in zip(tuple_one, tuple_two)]) # type: ignore