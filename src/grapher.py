"""
code to make graphs from network graphs.
"""
import networkx as nx
import matplotlib.pyplot as plt
import json
from networkx.readwrite import json_graph

class MapGraph:
    """
    Generates networkx graphs from UnrealIRCds /maps

    code is trash, but format is a pain to work with.
    """

    def __init__(self, data):
        """
        Create it.
        """
        stack = []
        batch = []
        for line in data.split('\n'):
            level, name = MapGraph.node_name(line)
            if name == '':
                continue

            if level >= len(stack):
                stack.append(name)
            else:
                stack = stack[:level]
                stack.append(name)
            
            if len(stack) > 1:
                batch.append((stack[-2], stack[-1]))

        self.graph = nx.Graph()
        self.graph.add_edges_from(batch)

    def json(self):
        return json.dumps(json_graph.node_link_data(self.graph))

    @staticmethod
    def node_name(line):
        """
        Reads a line and dumbs the node name
        """
        start = True
        name = ''
        level = 0
        for char in line:
            if start and char in ['`', '-', '|', ' ']:
                level += 1
                continue
            
            start = False

            if char in ['(', ' ']:
                break
            name += char
        return int(level/2), name

if __name__ == "__main__":
    plt.figure(figsize=(20, 20), dpi=80)
    g = MapGraph(open('./test.txt').read())
    nx.draw_kamada_kawai(g.graph, labels={node: node for node in g.graph.nodes()})
    plt.savefig('uwu.png')
