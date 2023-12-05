from utilities import read_file
import math

def part1(is_test: bool=True):
    if is_test:
        file = "data/day5_sample.txt"
    else:
        file = "data/day5.txt"

    all_lines = read_file(file)
    seeds, maps = clean_lines(all_lines)
    
    steps = []
    locations = []
    for seed in seeds:
        current_val = seed
        steps.append([current_val])

        for map in maps:
            for destination, source, length in map:
                if source <= current_val < source + length:
                    current_val = destination + current_val - source
                    break
            steps[-1].append(current_val)

        locations.append(current_val)

    return min(locations)

def clean_lines(all_lines):
    maps = []
    seeds = [int(x) for x in all_lines[0].split(': ')[1].split()]
    for line in all_lines[1:]:
        if line.strip() == '':
            maps.append([])
        elif line.strip().replace(' ', '').isnumeric():
            maps[-1].append([int(x) for x in line.split()])
        else:
            continue
    return seeds, maps

print(part1(False))
    

def part2(is_test: bool=True):
    if is_test:
        file = "data/day5_sample.txt"
    else:
        file = "data/day5.txt"

    all_lines = read_file(file)
    



#print(part2())