from bot import MyClient
from grapher import MapGraph
import networkx as nx
import matplotlib.pyplot as plt

import sys

if __name__ == "__main__":
    client = MyClient('testbot')
    client.run(sys.argv[1], tls=True)
    mapresp = client.getmap()
    g = MapGraph(mapresp)
    plt.figure(figsize=(32, 32), dpi=80)
    nx.draw_kamada_kawai(
        g.graph,
        labels={node: node for node in g.graph.nodes()}
    )
    plt.savefig(sys.argv[2])
