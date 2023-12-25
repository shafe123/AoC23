from utilities import get_lines
import networkx as nx
import matplotlib.pyplot as plt

def parse_input(lines: list[str]):
    graph = nx.Graph()
    for line in lines:
        source, neighbors = line.split(': ')
        neighbors = neighbors.split()
        graph.add_node(source)
        for neighbor in neighbors:
            graph.add_edge(source, neighbor)
    return graph

def make_cut(graph: nx.Graph, k: int):
    cutset = nx.minimum_edge_cut(graph)
    graph.remove_edges_from(cutset)
    a, b = nx.connected_components(graph)
    return a, b

def part1(is_test: bool = True):
    all_lines = get_lines(25, is_test)
    graph = parse_input(all_lines)
    sub1, sub2 = make_cut(graph, 3)
    return len(sub1) * len(sub2)


if __name__ == "__main__":
    print(part1(False))
    # print(part2(False))
