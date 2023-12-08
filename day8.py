from utilities import get_lines


def part1(is_test: bool = True):
    pattern, mapping = parse_file(is_test)

    count = 0

    location = "AAA"
    while location != "ZZZ":
        if pattern[count % len(pattern)] == "L":
            location = mapping[location][0]
        else:
            location = mapping[location][1]

        count += 1

    return count

def parse_file(is_test):
    all_lines = get_lines(8, is_test)
    pattern = all_lines.pop(0)
    all_lines.pop(0)

    mapping = {}
    start_location = ""
    for line in all_lines:
        location, places = line.split(' = ')

        if start_location == "":
            start_location = location

        places = places.replace('(', '').replace(')', '').split(', ')
        mapping[location] = tuple(places)
    return pattern, mapping


print(part1(False))


import math
def part2(is_test: bool = True):
    pattern, mapping = parse_file(is_test)
    As = [key for key in mapping if key[-1] == "A"]
    
    counts = []
    for A in As:
        location = A
        counts.append(0)
        
        while location[-1] != 'Z':
            if pattern[counts[-1] % len(pattern)] == "L":
                location = mapping[location][0]
            else:
                location = mapping[location][1]

            counts[-1] += 1

    return math.lcm(*counts)

print(part2(False))