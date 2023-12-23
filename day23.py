from utilities import get_lines, add_tuples, grid_string
from copy import deepcopy
from itertools import count
from tqdm import tqdm
import sys


class Node:
    def __init__(self, location, from_node, weight=1) -> None:
        self.weight = weight
        self.location = location
        self.to_nodes = []
        if from_node:
            self.from_nodes = [from_node]
            from_node.to_nodes.append(self)
        else:
            self.from_nodes = []
        self.is_goal = False

    def is_junction(self):
        return len(self.to_nodes) > 1

    def __str__(self) -> str:
        fine_print = [node.location for node in self.to_nodes]
        return f"{self.location} - {self.weight} - {fine_print}"

    def __repr__(self) -> str:
        return self.__str__()

    def __hash__(self) -> int:
        return hash(self.location)


def build_graph(grid, start, goal):
    nodes = {}
    nodes[start] = Node(start, None)

    to_visit = [nodes[start]]
    while to_visit:
        current_node = to_visit.pop()
        for neighbor in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            next_node = add_tuples(current_node.location, neighbor)
            if next_node == goal:
                nodes[goal] = Node(goal, current_node, 1)
                nodes[goal].is_goal = True
                continue
            if next_node in [node.location for node in current_node.from_nodes]:
                continue

            if (
                next_node[0] < 0
                or next_node[1] < 0
                or next_node[0] >= len(grid)
                or next_node[1] >= len(grid[0])
            ):
                continue

            character = grid[next_node[0]][next_node[1]]
            if character == "#":
                continue
            elif character == ".":
                add_node(to_visit, nodes, next_node, current_node)
            elif character == ">" and neighbor == (0, -1):
                continue
            elif character == "v" and neighbor == (-1, 0):
                continue
            elif character == ">":
                add_node(
                    to_visit, nodes, add_tuples(next_node, (0, 1)), current_node, 2
                )
            elif character == "v":
                add_node(
                    to_visit, nodes, add_tuples(next_node, (1, 0)), current_node, 2
                )

    return nodes


def add_node(
    queue: list[Node],
    map: dict[tuple[int, int], Node],
    next_location: tuple[int, int],
    current_node: Node,
    weight: int = 1,
):
    if next_location in map:
        next_node = map[next_location]
        next_node.from_nodes.append(current_node)
        current_node.to_nodes.append(next_node)
    else:
        new_node = Node(next_location, current_node, weight)
        map[next_location] = new_node
        queue.append(new_node)


def collapse_map(mapping: dict[tuple[int, int], Node]):
    to_visit = [mapping[(0, 1)]]

    while to_visit:
        current_node = to_visit.pop()

        # this is a 'to' branch
        if len(current_node.to_nodes) == 2:
            to_visit.extend(current_node.to_nodes)
            continue
        elif len(current_node.to_nodes) == 0:
            continue

        neighbor = current_node.to_nodes[0]
        # this is a 'from' branch
        if len(neighbor.from_nodes) == 2:
            if neighbor not in to_visit:
                to_visit.insert(0, neighbor)
            continue
        
        # otherwise, this is just one stop along a path with no branches
        if neighbor.is_goal:
            current_node.is_goal = neighbor.is_goal

        # update the neighbors' from nodes
        for neighbors_neighbor in neighbor.to_nodes:
            if neighbor in neighbors_neighbor.from_nodes:
                neighbors_neighbor.from_nodes.remove(neighbor)
            neighbors_neighbor.from_nodes.append(current_node)

        # update the node's weight and pointer
        current_node.weight += neighbor.weight
        current_node.to_nodes = neighbor.to_nodes.copy()

        # delete the neighbor from the maps
        if neighbor.location in mapping:
            del mapping[neighbor.location]

        to_visit.append(current_node)


def recurse(current_node: Node):
    if current_node.location == (0, 1):
        return current_node.weight

    result = [
        recurse(node) + current_node.weight for node in current_node.from_nodes
    ]
    return max(result)


def recurse_paths(mapping: dict[tuple[int, int], Node]):
    paths = []
    goal_node = None
    for node in mapping.values():
        if node.is_goal:
            goal_node = node

    return recurse(goal_node) - 1


def part1(is_test: bool = True):
    all_lines = get_lines(23, is_test)
    goal = (len(all_lines) - 1, len(all_lines[0]) - 2)
    winners = []
    all_nodes = build_graph(all_lines, (0, 1), goal)
    collapse_map(all_nodes)
    return recurse_paths(all_nodes)


if __name__ == "__main__":
    print(part1(False))
