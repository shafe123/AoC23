from utilities import read_file

def split_pulls(round: str) -> dict[str, int]:
    result = {}
    splits = round.split(', ')
    for pull in splits:
        num, color = pull.strip().split(' ')
        result[color] = int(num)
    return result

def can_play(pull: dict[str, int], colors = {'red': 12, 'green': 13, 'blue': 14}):
    for color, val in pull.items():
        if not (color in colors and colors[color] >= val):
            return False
    return True


def day2_part1(is_test: bool=True):
    if is_test:
        file = "data/day2_sample.txt"
    else:
        file = "data/day2.txt"
    
    all_lines = read_file(file)
    possible = []
    for line in all_lines:
        game_id, pulls = line.split(': ')
        game_id = int(game_id.split(' ')[1])

        pulls = pulls.split(';')
        
        works = True
        for pull in pulls:
            split_pull = split_pulls(pull)
            if not can_play(split_pull):
                works = False
                break

        if works:
            possible.append(game_id)
    
    return sum(possible)

def power_set(mins: dict[str, int]):
    product = 1
    for val in mins.values():
        product *= val
    return product

def day2_part2(is_test: bool=True):
    if is_test:
        file = "data/day2_sample.txt"
    else:
        file = "data/day2.txt"

    all_lines = read_file(file)

    sums = 0
    for line in all_lines:
        game_id, pulls = line.split(': ')
        game_id = int(game_id.split(' ')[1])

        pulls = pulls.split(';')
        
        works = True
        maxes = {}
        for pull in pulls:
            split_pull = split_pulls(pull)
            for color, val in split_pull.items():
                if color in maxes and maxes[color] < val:
                    maxes[color] = val
                elif color not in maxes:
                    maxes[color] = val

        power = power_set(maxes)
        sums += power
    return sums

        


print(day2_part2(False))