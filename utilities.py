def read_file(input_file: str, strip: bool = True) -> list[str]:
    result = []
    with open(input_file) as in_file:
        for line in in_file:
            if strip:
                line = line.strip()
            result.append(line)

    return result
