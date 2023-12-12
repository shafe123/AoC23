from utilities import get_lines, print_grid

# this is some black magic actually.
import functools


@functools.lru_cache(maxsize=None)
def count_permutations(conditions: str, current_run: int | None, groupings: tuple):
    if not conditions:
        # this was a successful set
        if current_run is None and len(groupings) == 0:
            return 1
        # end of a line like the first example
        if len(groupings) == 1 and current_run == groupings[0]:
            return 1
        return 0

    # how many more things are there?
    more_characters = conditions.count("#") + conditions.count("?")

    # base cases
    if current_run is None and more_characters < sum(groupings):
        return 0
    if current_run is not None and (
        more_characters + current_run < sum(groupings) or len(groupings) == 0
    ):
        return 0

    # start permutations
    counts = 0
    if conditions[0] == "." and current_run is not None:
        # end of a run
        if current_run != groupings[0]:
            return 0
        # this split didn't work, try next
        else:
            counts += count_permutations(conditions[1:], None, groupings[1:])

    # end of a run
    elif (
        conditions[0] == "?" and current_run is not None and current_run == groupings[0]
    ):
        counts += count_permutations(conditions[1:], None, groupings[1:])

    elif conditions[0] == "#" or conditions[0] == "?":
        # keep run going
        if current_run is not None:
            counts += count_permutations(conditions[1:], current_run + 1, groupings)
        # start of a run
        else:
            counts += count_permutations(conditions[1:], 1, groupings)

    # go next permutation like example 6
    if (conditions[0] == "?" or conditions[0] == ".") and current_run is None:
        counts += count_permutations(conditions[1:], None, groupings)
    
    return counts


def part1(is_test: bool = True):
    all_lines = get_lines(12, is_test)

    counts = []
    for line in all_lines:
        conditions, groupings = line.split()
        groupings = tuple([int(x) for x in groupings.split(",")])
        counts.append(count_permutations(conditions, None, groupings))

    return sum(counts)


# print(part1(False))


def part2(is_test: bool = True):
    all_lines = get_lines(12, is_test)

    counts = []
    for line in all_lines:
        conditions, groupings = line.split()
        conditions = "?".join([conditions] * 5)
        groupings = tuple([int(x) for x in groupings.split(",")]) * 5
        counts.append(count_permutations(conditions, None, groupings))

    return sum(counts)


print(part2(False))
