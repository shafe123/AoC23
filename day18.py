from utilities import get_lines, print_grid, add_tuples, grid_string
from enum import Enum
from tqdm import tqdm
from heapq import heappop, heappush
import copy
import math
import itertools


def mark_interior(start_point, grid, mark_character="*", guard_character="#"):
    grid = copy.deepcopy(grid)
    to_visit = [start_point]
    while to_visit:
        row, col = to_visit.pop(0)
        grid[row][col] = mark_character

        neighbors = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
        for new_row, new_col in neighbors:
            if (
                0 < new_row < len(grid)
                and 0 < new_col < len(grid[0])
                and (new_row, new_col) not in to_visit
                and grid[new_row][new_col] != guard_character
                and grid[new_row][new_col] != mark_character
            ):
                to_visit.append((new_row, new_col))
    return grid


def part1(is_test: bool = True):
    all_lines = get_lines(18, is_test)

    current_pos = (0, 0)
    min_x, min_y, max_x, max_y = 0, 0, 0, 0
    directions = []
    for line in all_lines:
        direction, distance, color = line.split()
        distance = int(distance)
        directions.append((direction, distance, color))

        match direction:
            case "R":
                current_pos = add_tuples(current_pos, (0, distance))
            case "L":
                current_pos = add_tuples(current_pos, (0, -distance))
            case "U":
                current_pos = add_tuples(current_pos, (-distance, 0))
            case "D":
                current_pos = add_tuples(current_pos, (distance, 0))

        if current_pos[0] < min_y:
            min_y = current_pos[0]
        if current_pos[0] > max_y:
            max_y = current_pos[0]
        if current_pos[1] < min_x:
            min_x = current_pos[1]
        if current_pos[1] > max_x:
            max_x = current_pos[1]

    grid = []
    y_diff = max_y - min_y + 1
    x_diff = max_x - min_x + 1
    for _ in range(y_diff):
        grid.append([])
        for _ in range(x_diff):
            grid[-1].append(".")

    # recreate '.' and '#'
    current_pos = (-min_y, -min_x)
    main_loop = []
    for direction, distance, color in tqdm(directions):
        match direction:
            case "U":
                for y_diff in range(distance):
                    grid[current_pos[0] - y_diff][current_pos[1]] = "#"
                    main_loop.append((current_pos[0] - y_diff, current_pos[1]))
                current_pos = add_tuples(current_pos, (-distance, 0))

            case "D":
                for y_diff in range(distance):
                    grid[current_pos[0] + y_diff][current_pos[1]] = "#"
                    main_loop.append((current_pos[0] + y_diff, current_pos[1]))
                current_pos = add_tuples(current_pos, (distance, 0))

            case "L":
                for x_diff in range(distance):
                    grid[current_pos[0]][current_pos[1] - x_diff] = "#"
                    main_loop.append((current_pos[0], current_pos[1] - x_diff))
                current_pos = add_tuples(current_pos, (0, -distance))

            case "R":
                for x_diff in range(distance):
                    grid[current_pos[0]][current_pos[1] + x_diff] = "#"
                    main_loop.append((current_pos[0], current_pos[1] + x_diff))
                current_pos = add_tuples(current_pos, (0, distance))
    grid[current_pos[0]][current_pos[1]] = "#"
    main_loop.append((current_pos[0], current_pos[1]))
    print_grid(grid)

    # I looked at my grid...
    new_grid = mark_interior((183, 1), grid)
    # print_grid(new_grid)
    return grid_string(new_grid).count("*") + len(main_loop) - 1


# if __name__ == "__main__":
#     print(part1(False))


def part2(is_test: bool = True):
    all_lines = get_lines(18, is_test)

    current_pos = (0, 0)
    directions = []
    nodes = []
    for line in all_lines:
        direction, distance, color = line.split()

        distance = int(color[2:7], base=16)
        direction = color[-2]
        mapping = { '0': 'R', '1': 'D', '2': 'L', '3': 'U'}
        direction = mapping[direction]

        directions.append((direction, distance, color))

        match direction:
            case "R":
                current_pos = add_tuples(current_pos, (0, distance))
            case "L":
                current_pos = add_tuples(current_pos, (0, -distance))
            case "U":
                current_pos = add_tuples(current_pos, (-distance, 0))
            case "D":
                current_pos = add_tuples(current_pos, (distance, 0))
        nodes.append(current_pos)

    # shoelace formula
    return picks(nodes)

def picks(nodes):
    A = shoelace(nodes)
    p = perimeter(nodes)
    return A + p / 2 + 1

def perimeter(nodes):
    perimeter = max(nodes[0][0], nodes[0][1])
    for (x0, y0), (x1, y1) in itertools.pairwise(nodes):
        perimeter += abs(x0 - x1) + abs(y0 - y1)
    return perimeter

def shoelace(nodes):
    total = 0
    for (x0, y0), (x1, y1) in itertools.pairwise(nodes):
        total += (y0 + y1) * (x0 - x1)
    total += (nodes[-1][0] + nodes[0][0]) * (nodes[-1][1] - nodes[0][1])
    return abs(total / 2)
    

if __name__ == "__main__":
    print(part2(False))