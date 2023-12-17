from utilities import get_lines, grid_string

def hash(input: str):
    hash_val = 0

    for char in input:
        if char == '\n':
            continue
        val = ord(char)
        hash_val = ((hash_val + val) * 17) % 256
    
    return hash_val

def part2(is_test: bool = True):
    all_lines = get_lines(15, is_test)

    all_steps = []
    boxes = []
    for _ in range(256):
        boxes.append([])

    for line in all_lines:
        steps = line.split(',')
        for cur_step in steps:
            if '-' in cur_step:
                lens = cur_step.split('-')[0]
            else:
                lens, lens_val = cur_step.split('=')
                lens_val = int(lens_val)
            
            hash_val = hash(lens)
            if '-' in cur_step:
                for index, l in enumerate(boxes[hash_val]):
                    if l[0] == lens:
                        boxes[hash_val].pop(index)
            else:
                for index, l in enumerate(boxes[hash_val]):
                    if l[0] == lens:
                        boxes[hash_val][index] = (lens, lens_val)
                        break
                else:
                    boxes[hash_val].append((lens, lens_val))

    
    return focusing_power(boxes)

def focusing_power(boxes: list[list[tuple[str, int]]]):
    all_vals = []
    for box_index, box in enumerate(boxes):
        for lens_index, lens in enumerate(box):
            current_val = (1 + box_index) * (lens_index + 1) * lens[1]
            all_vals.append(current_val)

    return sum(all_vals)

print(part2(False))
