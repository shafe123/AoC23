from utilities import get_lines

def clean_lines(all_lines: list[str]) -> list[int]:
    result = []
    for line in all_lines:
        values = [int(x) for x in line.split()]
        result.append(values)
    return result

def part1(is_test: bool = True):
    all_lines = get_lines(9, is_test)
    all_lines = clean_lines(all_lines)

    predictions = []
    for line in all_lines:
        differences = find_diff_chain(line)

        for index in range(len(differences) - 2, -1, -1):
            new_val = differences[index + 1][-1] + differences[index][-1]
            differences[index].append(new_val)
    
        predictions.append(differences[0][-1])

    return sum(predictions)

def find_diff_chain(line: list[int]) -> list[list[int]]:
    differences = [line.copy()]
    while any(x != 0 for x in differences[-1]):
        new_line = []
        for index, val in enumerate(differences[-1][:-1]):
            new_line.append(differences[-1][index + 1] - val)
        differences.append(new_line)
    differences[-1].append(0)
    return differences

print(part1(False))

def part2(is_test: bool = True):
    all_lines = get_lines(9, is_test)
    all_lines = clean_lines(all_lines)

    predictions = []
    for line in all_lines:
        differences = find_diff_chain(line)

        for index in range(len(differences) - 2, -1, -1):
            new_val = differences[index][0] - differences[index + 1][0]
            differences[index].insert(0, new_val)
    
        predictions.append(differences[0][0])

    return sum(predictions)

print(part2(False))