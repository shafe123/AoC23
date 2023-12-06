from utilities import read_file

def part1(is_test: bool=True):
    if is_test:
        file = "data/day6_sample.txt"
    else:
        file = "data/day6.txt"

    all_lines = read_file(file)


print(part1())