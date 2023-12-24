from utilities import get_lines, add_tuples, grid_string
from copy import deepcopy
from itertools import combinations
from tqdm import tqdm
import sys

def parse_input(lines: list[str]):
    result = []
    for line in lines:
        position, velocity = line.split(' @ ')
        position = tuple([int(x) for x in position.split(',')])
        velocity = tuple([int(x) for x in velocity.split(',')])
        result.append(position + velocity)
    return result

import sympy as sp
from sympy.solvers import solve

def calculate(vector_one: tuple, vector_two: tuple):
    # x1 + dx1 * t1 = x2 + dx2 * t2
    # y1 + dy1 * t1 = y2 + dy2 * t2
    x1, y1, z1, dx1, dy1, dz1 = vector_one
    x2, y2, z2, dx2, dy2, dz2 = vector_two
    t1, t2 = sp.symbols('t1 t2')
    eq1 = x1 + dx1 * t1 - x2 - dx2 * t2
    eq2 = y1 + dy1 * t1 - y2 - dy2 * t2
    soln = solve([eq1, eq2], [t1, t2], dict=True)
    if len(soln) == 1:
        if soln[0][t1] < 0 or soln[0][t2] < 0:
            return None

        x_intersect = x1 + dx1 * soln[0][t1]
        y_intersect = y1 + dy1 * soln[0][t1]
        return x_intersect, y_intersect


def part1(is_test: bool = True):
    all_lines = get_lines(24, is_test)
    hailstones = parse_input(all_lines)
    pairings = list(combinations(hailstones, 2))

    test_min, test_max = 200000000000000, 400000000000000
    collisions = []
    for vector_one, vector_two in tqdm(pairings):
        result = calculate(vector_one, vector_two)
        if result:
            x_interesct, y_intersect = result
            if test_min < x_interesct < test_max and test_min < y_intersect < test_max:
                collisions.append((vector_one, vector_two))
    return len(collisions)

def part2(is_test: bool = True):
    all_lines = get_lines(24, is_test)
    hailstones = parse_input(all_lines)
    solution = build_equations(hailstones)
    return solution

def build_equations(hailstones: list[tuple], grouping = 8):
    x, y, z, dx, dy, dz, t = sp.symbols('x y z dx dy dz t')
    solutions = []
    for offset in range(0, len(hailstones) - 1, grouping):
        equations = []
        t_symbols = []
        for index in range(8):
            x1, y1, z1, dx1, dy1, dz1 = hailstones[offset + index]  
            t_symbol = sp.symbols(f't_{index}')
            t_symbols.append(t_symbol)
            equations.append(x1 + dx1 * t_symbol - x - dx * t_symbol)
            equations.append(y1 + dy1 * t_symbol - y - dy * t_symbol)
            equations.append(z1 + dz1 * t_symbol - z - dz * t_symbol)
        print('solving...')
        solutions.extend(sp.solve(equations, t_symbols + [x, y, z, dx, dy, dz], dict=True))
        print(solutions[0][x] + solutions[0][y] + solutions[0][z])
        input('wait...')

if __name__ == "__main__":
    # print(part1(False))
    print(part2(False))
