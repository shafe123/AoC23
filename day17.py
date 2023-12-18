from utilities import get_lines, grid_string
from enum import Enum
from tqdm import tqdm
from heapq import heappop, heappush
import copy
import math


def enqueue(
    queue,
    grid,
    heat_loss: int,
    row: int,
    col: int,
    y_diff: int,
    x_diff: int,
    steps: int = 1,
):
    new_row = row + y_diff
    new_col = col + x_diff

    if not (0 <= new_row < len(grid) and 0 <= new_col < len(grid[new_row])):
        return

    heappush(
        queue,
        (
            heat_loss + grid[new_row][new_col],
            new_row,
            new_col,
            y_diff,
            x_diff,
            steps,
        ),
    )


def part2(is_test: bool = True):
    all_lines = get_lines(17, is_test)
    grid = [[int(x) for x in row] for row in all_lines]

    visited = set()
    # heat, row, col, direction-y, direction-x, length of setps
    priority_queue = [(0, 0, 0, 0, 0, 0)]

    while priority_queue:
        heat, row, col, y, x, step_length = heappop(priority_queue)

        if step_length >= 4 and row == len(grid) - 1 and col == len(grid[row]) - 1:
            return heat

        if (row, col, y, x, step_length) in visited:
            continue

        visited.add((row, col, y, x, step_length))

        if step_length < 10 and (y, x) != (0, 0):
            enqueue(priority_queue, grid, heat, row, col, y, x, step_length + 1)

        if step_length >= 4 or (y, x) == (0, 0):
            for neighbor_row, neighbor_col in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                if (neighbor_row, neighbor_col) != (y, x) and (neighbor_row, neighbor_col) != (-y, -x):
                    enqueue(priority_queue, grid, heat, row, col, neighbor_row, neighbor_col)


print(part2(False))
