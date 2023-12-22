from utilities import get_lines, add_tuples
from copy import deepcopy
from itertools import count
from tqdm import tqdm


def find_s(grid: list[str]):
    for row_index, row in enumerate(grid):
        if "S" in row:
            return (row_index, row.find("S"))


def part1(is_test: bool = True):
    all_lines = get_lines(21, is_test)
    start_point = find_s(all_lines)

    next_visit = [start_point]
    to_visit = []
    last_visit = []

    for i in tqdm(range(26501365)):
        to_visit = deepcopy(next_visit)
        last_visit = deepcopy(to_visit)
        next_visit = []

        while to_visit:
            current_point = to_visit.pop()
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
                    next_visit.append(next_point)

        next_visit = list(set(next_visit))

    return len(next_visit)


if __name__ == "__main__":
    print(part1(False))
