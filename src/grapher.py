"""
code to make graphs from network graphs.
"""
import networkx as nx
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
        self.graph = nx.Graph()
        self.graph.add_edges_from(data)

    def json(self):
        return json.dumps(json_graph.node_link_data(self.graph))
