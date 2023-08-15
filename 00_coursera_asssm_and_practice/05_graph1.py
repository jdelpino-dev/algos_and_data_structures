"""
Graph DS implementation #1

This implementation creats a class called Graph that allows to create
graphs and multigraphs. It does't support weighted edges, but it supports
multiedges.

It is a efficient implementation for sparse graphs and for
operations that involve the whole graph. For example, it is very efficient
to add and delete a node or an edge, and also to contract an edge or to
fuse two nodes. I desinged it to be used in my implementation of
the Karger's algorithm for finding the minimum cut of a graph.

The class graph includes basic methods to add nodes and edges,
as well as more advanced methods like cutting edges,fusing nodes,
delete loops, etc.

It is also a factory of graphs, as it can create graphs from files,
list of edges, from a list of nodes, from a list of edges, etc.

It uses a 2 dictionary of dictionaries as underlying data structure:

    (1) Dictionary of nodes: a dictionary of dictionaries that
    maps each node to a dictionary of its neighbors. Each neighbor's
    value is a counter of the number of edges that connects it to the
    node.

    (2) Dictionary of edges: it maps edges to their counter of how many
    multiple edges each of them represents. If the graph is a simple graph,
    then the counter is always 1.

The basic data element of this structures are the edges, which are
represented as tuples of nodes and the nodes are represented as strings
or numbers.
"""

from typing import Union, Tuple, Dict

# Defines the type primitives of the graph
node_type = Union[str, int]
edge_type = Tuple[Union[str, int], Union[str, int]]
nodes_dict = Dict[node_type, Dict[node_type, int]]
edges_dict = Dict[edge_type, int]

# Defines the graph class


class Graph (type="multigraph"):
    def __init__(self):
        """Initializes a graph object.
        """
        self._nodes_dict: nodes_dict = {}
        self._edges_dict: edges_dict = {}
        self._type = type

    def __len__(self) -> int:
        """Returns the number of nodes of the graph.
        """
        return len(self._nodes_dict)

    def num_nodes(self) -> int:
        """Returns the number of nodes of the graph.
        """
        return len(self._nodes_dict)

    def num_edges(self) -> int:
        """Returns the number of edges of the graph.
        """
        return len(self._edges_dict)

    def size(self) -> tuple:
        """Returns the number of edges of the graph.
        """
        return (self.num_nodes(), self.num_edges())

    def is_multigraph(self) -> bool:
        """Returns True if the graph is a multigraph.
        """
        return self._type == "multigraph"

    def nodes(self) -> nodes_dict:
        """Returns the nodes of the graph.
        """
        return self._nodes_dict

    def edges(self) -> edges_dict:
        """Returns the edges of the graph.
        """
        return self._edges_dict

    def node_list(self) -> list:
        """Returns the list of nodes of the graph.
        """
        return list(self._nodes_dict.keys())

    def edge_list(self) -> list:
        """Returns the list of edges of the graph.
        """
        return list(self._edges_dict.keys())

    def neighbors_list(self, node: type) -> list:
        """Returns the list of neighbors of a node.
        """
        return list(self._nodes_dict[node].keys())
