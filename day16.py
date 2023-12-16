from utilities import get_lines, grid_string
from enum import Enum
from tqdm import tqdm
import copy

class Direction(Enum):
    Left = (0, -1)
    Right = (0, 1)
    Up = (-1, 0)
    Down = (1, 0)

def add_tuples(tuple1, tuple2):
    assert len(tuple1) == len(tuple2)
    vals = []
    for index in range(len(tuple1)):
        vals.append(tuple1[index] + tuple2[index])
    return tuple(vals)

class Beam():
    def __init__(self, position: tuple[int, int], direction: Direction) -> None:
        self.position = position
        self.direction = direction

    def move(self) -> tuple[int, int]:
        self.position = add_tuples(self.direction.value, self.position)
        return self.position

    def rotate_right(self):
        match self.direction:
            case Direction.Left:
                self.direction = Direction.Up
            case Direction.Up:
                self.direction = Direction.Right
            case Direction.Right:
                self.direction = Direction.Down
            case Direction.Down:
                self.direction = Direction.Left

    def rotate_left(self):
        match self.direction:
            case Direction.Left:
                self.direction = Direction.Down
            case Direction.Up:
                self.direction = Direction.Left
            case Direction.Right:
                self.direction = Direction.Up
            case Direction.Down:
                self.direction = Direction.Right

    def split(self):
        self.rotate_left()
        new_beam = Beam(self.position, self.direction)
        new_beam.rotate_right()
        new_beam.rotate_right()
        return new_beam
        

def part2(is_test: bool = True):
    all_lines = get_lines(16, is_test)

    right_beams = [Beam((row, 0), Direction.Right) for row in range(len(all_lines))]
    left_beams = [Beam((row, len(all_lines[0]) - 1), Direction.Left) for row in range(len(all_lines))]
    up_beams = [Beam((len(all_lines) - 1, col), Direction.Up) for col in range(len(all_lines[0]))]
    down_beams = [Beam(((0, col)), Direction.Down) for col in range(len(all_lines[0]))]
    possible_beams = right_beams + left_beams + up_beams + down_beams

    has_moved = True
    energized_list = []
    last_ten = [-9,-8,-7,-6,-5,-4,-3,-2,-1,0]

    for index, beam in enumerate(tqdm(possible_beams)):
        all_beams = set([beam])
        has_moved = True

        energized = []
        for index, line in enumerate(all_lines):
            all_lines[index] = list(line)
            energized.append(['.'] * len(line))

        while has_moved:
            has_moved = one_step(all_lines, energized, all_beams)
            last_ten.pop(0)
            last_ten.append(grid_string(energized).count('#'))

            if len(set(last_ten)) == 1:
                energized_list.append(last_ten[-1])
                break

    return max(energized_list)

def one_step(all_lines: list[list[str]], energized: list[list[str]], all_beams: set[Beam]):
    has_moved = False
    to_remove = []
    to_add = []
    for beam in all_beams:
        if beam.position[0] < 0 or beam.position[0] >= len(all_lines) or beam.position[1] < 0 or beam.position[1] >= len(all_lines[0]):
            to_remove.append(beam)
            continue

        energized[beam.position[0]][beam.position[1]] = '#'
        location = all_lines[beam.position[0]][beam.position[1]]
            
        if location == '|' and (beam.direction == Direction.Left or beam.direction == Direction.Right):
            to_add.append(beam.split())
        elif location == '-' and (beam.direction == Direction.Up or beam.direction == Direction.Down):
            to_add.append(beam.split())
        elif location == '\\' and (beam.direction == Direction.Up or beam.direction == Direction.Down):
            beam.rotate_left()
        elif location == '\\' and (beam.direction == Direction.Right or beam.direction == Direction.Left):
            beam.rotate_right()
        elif location == '/' and (beam.direction == Direction.Right or beam.direction == Direction.Left):
            beam.rotate_left()
        elif location == '/' and (beam.direction == Direction.Up or beam.direction == Direction.Down):
            beam.rotate_right()

        has_moved = True
        beam.move()

    for beam in to_remove:
        all_beams.remove(beam)
    for beam in to_add:
        all_beams.add(beam)
    
    return has_moved


print(part2(False))