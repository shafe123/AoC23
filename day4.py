from utilities import read_file

def day4_part1(is_test: bool=True):
    if is_test:
        file = "data/day4_sample.txt"
    else:
        file = "data/day4.txt"

    all_lines = read_file(file)
    values = []
    for line in all_lines:
        winning_numbers, my_numbers = line.split(': ')[1].split(' | ')
        winning_numbers = set(winning_numbers.split())
        my_numbers = set(my_numbers.split())
        intersect = winning_numbers.intersection(my_numbers)

        if len(intersect) != 0:
            value = 2 ** (len(intersect) - 1)
        else:
            value = 0
        values.append(value)
    return sum(values)

        
    
    
def day4_part2(is_test: bool=True):
    if is_test:
        file = "data/day4_sample.txt"
    else:
        file = "data/day4.txt"

    all_lines = read_file(file)


print(day4_part1(False))