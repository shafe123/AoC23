from utilities import get_lines, print_grid

def find_mirror(pattern: list[list[str]]):
    # vertical split
    last_attempt = 0
    row = pattern[0]

    while last_attempt < len(row) - 1:
        row = pattern[0]
        split = -1
        for index in range(last_attempt, len(row)-1):
            last_attempt = index + 1
            one, two = split_list(row, index)
            if one != two:
                continue
            else:
                split = index
                break

        if split != -1:
            is_valid = True
            for row in pattern[1:]:
                one, two = split_list(row, split)
                if one != two:
                    is_valid = False
                    break
            if is_valid: 
                return 'vertical', split
        
    # horizontal split
    for index, row in enumerate(pattern):
        one, two = split_list(pattern, index)
        
        if one != two:
            continue
        else:
            return 'horizontal', index


def split_list(input_list, index):
    one, two = input_list[:index + 1][::-1], input_list[index + 1:]
    one = one[:min(len(one), len(two))]
    two = two[:min(len(one), len(two))]
    return one, two


def part1(is_test: bool = True):
    all_lines = get_lines(13, is_test)
    patterns = []
    last_index = 0
    for index, line in enumerate(all_lines):
        if line == '':
            patterns.append(all_lines[last_index:index])
            last_index = index + 1
    patterns.append(all_lines[last_index:])

    splits = []
    for index, pattern in enumerate(patterns):
        splits.append((index, *find_mirror(pattern)))

    count = 0
    for split in splits:
        if split[1] == 'vertical':
            count += (split[2] + 1)
        else:
            count += (split[2] + 1) * 100
    return count

def find_mirror_with_error(pattern: list[list[str]]):
    # vertical split
    last_attempt = 0
    row = pattern[0]

    while last_attempt < len(row) - 1:
        row = pattern[0]
        split = -1
        for index in range(last_attempt, len(row)-1):
            last_attempt = index + 1
            one, two = split_list(row, index)
            errors = 0

            for char_index in range(len(one)):
                if one[char_index] != two[char_index]:
                    errors += 1

            if errors > 1:
                continue
            else:
                split = index
                break

        if split != -1:
            is_valid = True
            for row in pattern[1:]:
                one, two = split_list(row, split)
                for char_index in range(len(one)):
                    if one[char_index] != two[char_index]:
                        errors += 1
                
                if errors > 1:
                    is_valid = False
                    break
            if is_valid and errors == 1: 
                return 'vertical', split
        
    # horizontal split
    for index, row in enumerate(pattern):
        one, two = split_list(pattern, index)
        errors = 0
        
        for line_index in range(len(one)):
            for char_index in range(len(one[line_index])):
                if one[line_index][char_index] != two[line_index][char_index]:
                    errors +=1 
        if errors != 1:
            continue
        else:
            return 'horizontal', index

def part2(is_test: bool = True):
    all_lines = get_lines(13, is_test)
    patterns = []
    last_index = 0
    for index, line in enumerate(all_lines):
        if line == '':
            patterns.append(all_lines[last_index:index])
            last_index = index + 1
    patterns.append(all_lines[last_index:])

    splits = []
    for index, pattern in enumerate(patterns):
        splits.append((index, *find_mirror_with_error(pattern)))

    count = 0
    for split in splits:
        if split[1] == 'vertical':
            count += (split[2] + 1)
        else:
            count += (split[2] + 1) * 100
    return count

print(part2(False))
