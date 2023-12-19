from utilities import get_lines
from copy import deepcopy
from functools import reduce

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

def product(input: list):
    return reduce(lambda x, y: x * y, input)

def part2(is_test: bool = True):
    all_lines = get_lines(19, is_test)
    separator = all_lines.index('')
    workflows = extract_workflows(all_lines[:separator])
    parts = extract_parts(all_lines[separator + 1:])

    start_range = (1, 4000)
    start_workflow = 'in'
    initial_ranges = {'x': start_range, 'm': start_range, 'a': start_range, 's': start_range}
    successful_runs = []
    to_visit = [(deepcopy(initial_ranges), start_workflow)]
    while to_visit:
        ranges, workflow_name = to_visit.pop()
        for condition, result in workflows[workflow_name]:
            new_range = deepcopy(ranges)
            if condition:
                # we need to bring down the upper limit
                if condition.comparison == '<':

                    # but only if the upper limit is below our current limit
                    if condition.value < new_range[condition.variable][1]:
                        new_range[condition.variable] = (ranges[condition.variable][0], condition.value - 1)
                        ranges[condition.variable] = (condition.value, ranges[condition.variable][1])

                # same but greater than
                elif condition.comparison == '>':
                    if condition.value > new_range[condition.variable][0]:
                        new_range[condition.variable] = (condition.value + 1, ranges[condition.variable][1])
                        ranges[condition.variable] = (ranges[condition.variable][0], condition.value)
                
                # investigate the next workflow
                if result not in ['A', 'R']:
                    to_visit.append((new_range, result))

            if result == 'A':
                successful_runs.append(deepcopy(new_range))
            
            if not condition and result not in ['A', 'R']:
                to_visit.append((new_range, result))

    total = 0
    for range_dict in successful_runs:
        total += product([maximum - minimum + 1 for minimum, maximum in range_dict.values()])
    return total


if __name__ == "__main__":
    # print(part1(False))
    print(part2(False))