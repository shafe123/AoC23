from utilities import get_lines, add_tuples
from copy import deepcopy
from itertools import count
from tqdm import tqdm


def brick_letter(column_int: int):
    start_index = 0  #  it can start either at 0 or at 1
    letter = ""
    while column_int > 25 + start_index:
        letter += chr(65 + int((column_int - start_index) / 26) - 1)
        column_int = column_int - (int((column_int - start_index) / 26)) * 26
    letter += chr(65 - start_index + (int(column_int)))
    return letter


class Brick:
    def __init__(self, name, start_point, end_point) -> None:
        self.name = name
        self.start = start_point
        self.end = end_point
        self.xs = set(list(range(self.start[0], self.end[0] + 1)))
        self.ys = set(list(range(self.start[1], self.end[1] + 1)))
        self.zs = sorted(list(range(self.start[2], self.end[2] + 1)))
        self.supports = []
        self.supported_by = []

    def update_endpoints(self):
        self.start = (min(self.xs), min(self.ys), min(self.zs))
        self.end = (max(self.xs), max(self.ys), max(self.zs))

    def intersects(self, other):
        return self.xs.intersection(other.xs) and self.ys.intersection(other.ys)

    def __str__(self) -> str:
        return f"{self.name}: {self.start} - {self.end}"

    def __repr__(self) -> str:
        return self.__str__()
    
    def __hash__(self) -> int:
        return hash(self.name)


def parse_input(input_lines: list[str]):
    bricks = []
    for index, line in enumerate(input_lines):
        start, end = line.split("~")
        start = tuple([int(x) for x in start.split(",")])
        end = tuple([int(x) for x in end.split(",")])

        bricks.append(Brick(brick_letter(index), start, end))
    return bricks


def fall_bricks(all_bricks: list[Brick]):
    # sort in z-order
    all_bricks.sort(key=lambda brick: brick.zs[0])

    for index, brick in enumerate(all_bricks):
        is_supported = False

        for lower in range(index - 1, -1, -1):
            lower_brick = all_bricks[lower]
            if not is_supported and brick.intersects(lower_brick):
                # this will be supported by the lower brick
                lower_brick.supports.append(brick)
                brick.supported_by.append(lower_brick)

                # fall the z-value down
                brick.zs = [
                    lower_brick.zs[-1] + z_index + 1 for z_index in range(len(brick.zs))
                ]
                brick.update_endpoints()

                is_supported = True

            # check if any other bricks also support
            elif (
                is_supported
                and lower_brick.zs[-1] == brick.zs[0] - 1
                and brick.intersects(lower_brick)
            ):
                lower_brick.supports.append(brick)
                brick.supported_by.append(lower_brick)
        
        if not is_supported:
            brick.zs = [1 + z_index for z_index in range(len(brick.zs))]
            brick.update_endpoints()



def find_removable(bricks: list[Brick]):
    removable = []

    for brick in bricks:
        if not brick.supports:
            removable.append(brick)
        for supported in brick.supports:
            if len(supported.supported_by) > 1:
                removable.append(brick)

    return set(removable)


def part1(is_test: bool = True):
    all_lines = get_lines(22, is_test)
    all_bricks = parse_input(all_lines)
    fall_bricks(all_bricks)
    removable = find_removable(all_bricks)
    return len(removable)


if __name__ == "__main__":
    print(part1(False))
