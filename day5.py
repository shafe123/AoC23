from utilities import read_file
import math

def part1(is_test: bool=True):
    if is_test:
        file = "data/day5_sample.txt"
    else:
        file = "data/day5.txt"

    all_lines = read_file(file)
    seeds, maps = clean_lines(all_lines)
    locations = map_seeds(seeds, maps)

    return min(locations)

def map_seeds(seeds, maps):
    locations = []
    for seed in seeds:
        current_val = seed

        for map in maps:
            for destination, source, length in map:
                if source <= current_val < source + length:
                    current_val = destination + current_val - source
                    break

        locations.append(current_val)
    return locations

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
    
def map_seed_range(seed_ranges: list[tuple[int, int]], maps):
    locations = []

    while seed_ranges:
        input_range = seed_ranges.pop()
        
        for map in maps:
            for destination, source, length in map:
                if len(input_range) == 0:
                    break
                source_range = (source, source + length - 1)

                # left = (start, min(end, source))
                # mid = (max(start, source), min(source_end, end))
                # right = (max(source_end, start), end)

                # if left[1] > left[0]:
                #     seed_ranges.append(left)
                # if mid[1] > mid[0]:
                #     locations.append((mid[0] - source + destination, mid[1] - source + destination))
                # if right[1] > right[0]:
                #     seed_ranges.append(right)

    return locations
        


def part2(is_test: bool=True):
    if is_test:
        file = "data/day5_sample.txt"
    else:
        file = "data/day5.txt"

    all_lines = read_file(file)
    original_seeds, maps = clean_lines(all_lines)
    seed_ranges = list(zip(original_seeds[::2], original_seeds[1::2]))
    locations = map_seed_range(seed_ranges, maps)

    return min(locations)



print(part2(True))