from utilities import read_file
import math

def part1(is_test: bool=True):
    if is_test:
        file = "data/day6_sample.txt"
    else:
        file = "data/day6.txt"

    all_lines = read_file(file)
    times = [int(x) for x in all_lines[0][10:].split()]
    distances = [int(x) for x in all_lines[1][10:].split()]

    races = zip(times, distances)

    all_wins = []
    for time, record in races:
        possible_wins = []

        start_point_left = math.floor(time / 2)
        start_point_right = math.ceil(time / 2)

        if start_point_left == start_point_right:
            start_point_right += 1

        initial_left_distance = calculate_distance(start_point_left, time)
        while initial_left_distance > record:
            possible_wins.append(initial_left_distance)
            start_point_left -= 1
            initial_left_distance = calculate_distance(start_point_left, time)

        initial_right_distance = calculate_distance(start_point_right, time)
        while initial_right_distance > record:
            possible_wins.append(initial_right_distance)
            start_point_right += 1
            initial_right_distance = calculate_distance(start_point_right, time)

        all_wins.append(len(possible_wins))
    
    product = 1
    for counts in all_wins:
        product *= counts
    return product

        
def calculate_distance(velocity, time):
    time_remaining = time - velocity
    distance = velocity * time_remaining
    return distance

# print(part1(False))

def part2(is_test: bool=True):
    if is_test:
        file = "data/day6_sample.txt"
    else:
        file = "data/day6.txt"

    all_lines = read_file(file)
    time = int(all_lines[0][10:].replace(' ', ''))
    record = int(all_lines[1][10:].replace(' ', ''))
    print(time, record)

    possible_wins = []

    start_point_left = math.floor(time / 2)
    start_point_right = math.ceil(time / 2)

    if start_point_left == start_point_right:
        start_point_right += 1

    initial_left_distance = calculate_distance(start_point_left, time)
    while initial_left_distance > record:
        possible_wins.append(initial_left_distance)
        start_point_left -= 1
        initial_left_distance = calculate_distance(start_point_left, time)
    
    return len(possible_wins) * 2 if start_point_left != start_point_right else len(possible_wins) * 2 + 1


print(part2(False))