from utilities import get_lines, add_tuples
from copy import deepcopy
from itertools import count
from tqdm import tqdm
import sys

sys.setrecursionlimit(100000000)
def search(grid: list[str], visited: list[tuple[int, int]], current_node: tuple[int,int], goal: tuple[int, int], successes: list[list[tuple[int, int]]]):
    if grid[current_node[0]][current_node[1]] == '>':
        new_visited = deepcopy(visited)
        new_visited.append(current_node)
        search(grid, new_visited, add_tuples(current_node, (0, 1)), goal, successes)
        return
    
    if grid[current_node[0]][current_node[1]] == 'v':
        new_visited = deepcopy(visited)
        new_visited.append(current_node)
        search(grid, new_visited, add_tuples(current_node, (1, 0)), goal, successes)
        return

    for neighbor in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        next_node = add_tuples(current_node, neighbor)
        if next_node == goal:
            successes.append(visited)
            continue

        if next_node in visited:
            continue
        if next_node[0] < 0 or next_node[1] < 0 or next_node[0] >= len(grid) or next_node[1] >= len(grid[0]):
            continue

        character = grid[next_node[0]][next_node[1]]
        if character == '#':
            continue
        if character == '>' and neighbor == (0, -1):
            continue
        if character == 'v' and neighbor == (-1, 0):
            continue

        new_visited = deepcopy(visited)
        new_visited.append(current_node)
        search(grid, new_visited, next_node, goal, successes)


def part1(is_test: bool = True):
    all_lines = get_lines(23, is_test)
    goal = (len(all_lines) - 1, len(all_lines[0]) - 2)
    winners = []
    search(all_lines, [], (0, 1), goal, winners)
    # for winner in winners:
    #     print(len(winner) + 1)
    return max([len(winner) + 1 for winner in winners])



if __name__ == "__main__":
    print(part1(False))
