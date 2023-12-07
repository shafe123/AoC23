def read_file(input_file: str, strip: bool = True) -> list[str]:
    result = []
    with open(input_file) as in_file:
        for line in in_file:
            if strip:
                line = line.strip()
            result.append(line)

    return result

def get_lines(day: int, is_test: bool) -> list[str]:
    if is_test:
        file = f"data/day{day}_sample.txt"
    else:
        file = f"data/day{day}.txt"

    return read_file(file)