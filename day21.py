from utilities import get_lines, add_tuples
from copy import deepcopy
from itertools import count
from tqdm import tqdm


def find_s(grid: list[str]):
    for row_index, row in enumerate(grid):
        if "S" in row:
            return (row_index, row.find("S"))


def part2(is_test: bool = True):
    all_lines = get_lines(21, is_test)
    start_point = find_s(all_lines)

    next_visit = set([start_point])
    tick_tocks = [next_visit]

    for i in tqdm(range(26501365)):
        tick_tocks.append(set())
        for current_point in tick_tocks[i]:
            for neighbor in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                next_point = add_tuples(current_point, neighbor)
                new_row = (
                    next_point[0] % len(all_lines)
                    if next_point[0] >= 0
                    else next_point[0] % len(all_lines) - len(all_lines)
                )
                new_col = (
                    next_point[1] % len(all_lines[0])
                    if next_point[1] >= 0
                    else next_point[1] % len(all_lines[0]) - len(all_lines[0])
                )
                if (
                    all_lines[new_row][new_col] == "#"
                ):
                    continue
                else:
                    if next_point not in tick_tocks[i - 1]:
                        tick_tocks[i + 1].add(next_point)

    total_count = sum([len(tick) for tick in tick_tocks[::-2]])
    return total_count


if __name__ == "__main__":
    print(part2())
