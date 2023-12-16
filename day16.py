from utilities import get_lines, grid_string
from enum import Enum
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
        

def part1(is_test: bool = True):
    all_lines = get_lines(16, is_test)

    energized = []
    for index, line in enumerate(all_lines):
        all_lines[index] = list(line)
        energized.append(['.'] * len(line))

    all_beams = [Beam((0, 0), Direction.Right)]
    has_moved = True
    while has_moved:
        has_moved = False
        to_remove = []
        for index, beam in enumerate(all_beams):
            if beam.position[0] < 0 or beam.position[0] >= len(all_lines) or beam.position[1] < 0 or beam.position[1] >= len(all_lines[0]):
                to_remove.append(index)
                continue

            energized[beam.position[0]][beam.position[1]] = '#'
            location = all_lines[beam.position[0]][beam.position[1]]
            
            if location == '|' and (beam.direction == Direction.Left or beam.direction == Direction.Right):
                all_beams.append(beam.split())
            elif location == '-' and (beam.direction == Direction.Up or beam.direction == Direction.Down):
                all_beams.append(beam.split())
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

        to_remove.sort(reverse=True)
        for index in to_remove:
            all_beams.pop(index)

        print(grid_string(energized).count('#'))


print(part1(False))