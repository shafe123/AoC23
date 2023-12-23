from utilities import get_lines, add_tuples, grid_string
from copy import deepcopy
from itertools import count
from tqdm import tqdm
import sys

class Node:
    def __init__(self, location, from_node, weight = 1) -> None:
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
        return f'{self.location} - {self.weight}'
    
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
            if next_node in [node.location for node in current_node.from_nodes]:
                continue

            if next_node[0] < 0 or next_node[1] < 0 or next_node[0] >= len(grid) or next_node[1] >= len(grid[0]):
                continue
            
            character = grid[next_node[0]][next_node[1]]
            if character == '#':
                continue
            elif character == '.':
                add_node(to_visit, nodes, next_node, current_node)
            elif character == '>' and neighbor == (0, -1):
                continue
            elif character == 'v' and neighbor == (-1, 0):
                continue
            elif character == '>':
                add_node(to_visit, nodes, add_tuples(next_node, (0, 1)), current_node, 2)
            elif character == 'v':
                add_node(to_visit, nodes, add_tuples(next_node, (1, 0)), current_node, 2)

    return nodes

def add_node(queue: list[Node], map: dict[tuple[int, int], Node], next_location: tuple[int, int], current_node: Node, weight: int = 1):
    if next_location in map:
        next_node = map[next_location]
        next_node.from_nodes.append(current_node)
    else:
        new_node = Node(next_location, current_node, weight)
        map[next_location] = new_node
        queue.append(new_node)
    
def collapse_map(mapping: dict[tuple[int, int], Node]):
    deleted = []
    to_delete = list(mapping.keys())
    while to_delete:
        location = to_delete.pop(0)
        node = mapping[location]


        while len(node.to_nodes) == 1 and len(node.to_nodes[0].from_nodes) <= 1:
            neighbor = node.to_nodes[0]
            if neighbor.is_goal:
                node.is_goal = neighbor.is_goal

            # update the next nodes weight and pointer
            node.weight += neighbor.weight
            node.to_nodes = neighbor.to_nodes.copy()
            
            # update the next nodes neighbors from node
            for neighbors_neighbor in neighbor.to_nodes:
                neighbors_neighbor.from_nodes.remove(neighbor)
                neighbors_neighbor.from_nodes.append(node)

            deleted.append(neighbor.location)
            del mapping[neighbor.location]
            if neighbor.location in to_delete:
                to_delete.remove(neighbor.location)

def recurse_paths(mapping: dict[tuple[int, int], Node]):
    pass


def part1(is_test: bool = True):
    all_lines = get_lines(23, is_test)
    goal = (len(all_lines) - 1, len(all_lines[0]) - 2)
    winners = []
    all_nodes = build_graph(all_lines, (0, 1), goal)
    collapse_map(all_nodes)
    string = grid_string(all_lines)
    print(string.count('.'),string.count('>'),string.count('v'))
    print(len(all_nodes))



if __name__ == "__main__":
    print(part1())
