from utilities import get_lines, print_grid, add_tuples, grid_string
from enum import Enum
from tqdm import tqdm
from heapq import heappop, heappush
import copy
import math
import itertools

class Condition():
    def __init__(self, condition) -> None:
        self.variable = condition[0]
        self.comparison = condition[1]
        self.value = int(condition[2:])

    def check_input(self, input: dict[str, int]) -> bool:
        if self.comparison == '<':
            return input[self.variable] < self.value
        else:
            return input[self.variable] > self.value

def extract_parts(input: list[str]) -> list[dict[str, int]]:
    result = []
    for line in input:
        values = {}
        line = line.replace('{', '').replace('}', '')
        parts = line.split(',')
        for part in parts:
            letter, number = part.split('=')
            values[letter] = int(number)
        result.append(values)

    return result

def check_part(part: dict[str, int], workflows: dict[str, list[tuple[Condition, str]]]) -> str:
    result = 'in'
    while result not in ['A', 'R']:
        for rule in workflows[result]:
            if rule[0] == None:
                result = rule[1]
                break
            
            elif rule[0].check_input(part):
                result = rule[1]
                break
    return result


def part1(is_test: bool = True):
    all_lines = get_lines(19, is_test)
    separator = all_lines.index('')
    workflows = extract_workflows(all_lines[:separator])
    parts = extract_parts(all_lines[separator + 1:])

    results = []
    for index, part in enumerate(parts):
        results.append((check_part(part, workflows), part))
    
    total = 0
    for result, part in results:
        if result == 'A':
            total += sum(part.values())
    return total


def extract_workflows(all_lines: list[str]) -> dict[str, list[tuple[Condition, str]]]:
    workflows = {}
    for line in all_lines:
        name, original_rules = line[:-1].split('{')
        original_rules = original_rules.split(',')
        rules = []
        for rule in original_rules:
            if ':' in rule:
                condition, result = rule.split(':')
                rules.append((Condition(condition), result))
            else:
                rules.append((None, rule))
        workflows[name] = rules
    return workflows

if __name__ == "__main__":
    print(part1(False))