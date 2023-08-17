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
from random import seed, choice
import copy

# Defines the type primitives for the graph class
Node = Union[str, int]
Edge = Tuple[Node, Node]
GraphElement = Union[Node, Edge]
NeighboorDict = Dict[Node, int]
NodeDict = Dict[Node, NeighboorDict]
EdgeDict = Dict[Edge, int]
ElementDict = Union[NodeDict, EdgeDict]
ElementValue = Union[NeighboorDict, int]

# Defines the graph class


class Graph:
    def __init__(self, directed: bool = False, multigraph: bool = False):
        """Initializes a graph object.
        """
        self._nodes_dict: NodeDict = {}
        self._edges_dict: EdgeDict = {}
        self._directed = directed
        self._multigraph = multigraph

    def __len__(self) -> int:
        """Returns the number of nodes of the graph.
        """
        return len(self._nodes_dict)

    def __contains__(self, element: GraphElement) -> bool:
        """Returns True if the element is in the graph.
        """
        if self._is_node(element):
            return element in self._nodes_dict
        elif self._is_edge(element):
            if self._directed:
                return element in self._edges_dict
            else:
                return (element in self._edges_dict
                        or self._invert_edge(element) in self._edges_dict)
        else:
            raise TypeError("Element must be a valid node (string or int)"
                            "or an edge (tuple of nodes)")

    def __iter__(self):
        """Returns an iterator for the nodes of the graph.
        """
        return iter(self._nodes_dict.keys())

    def __del__(self):
        """Deletes the graph.
        """
        del self._nodes_dict
        del self._edges_dict

    def __getitem__(self, element: GraphElement) -> NeighboorDict:
        """Returns the neighbors of a node or the counter of an edge.
        """
        if element in self:
            if self._is_node(element):
                return self._nodes_dict[element]
            elif self._is_edge(element):
                if self._directed:
                    return self._edges_dict[element]
                else:
                    if element in self._edges_dict:
                        return self._edges_dict[element]
                    else:
                        return self._edges_dict[self._invert_edge(element)]

    def _is_inverse_edge(self, edge: Edge) -> bool:
        """Returns True if the edge is the inverse of another edge.
        """
        inverse_edge = tuple(list(edge)[::-1])
        return inverse_edge in self._edges_dict

    def _invert_edge(self, edge: Edge) -> Edge:
        """Returns the inverse of an edge.
        """
        return tuple(list(edge)[::-1])

    @property
    def nodes(self) -> NodeDict:
        """Returns the nodes of the graph.
        """
        return self._nodes_dict

    @property
    def edges(self) -> EdgeDict:
        """Returns the edges of the graph.
        """
        return self._edges_dict

    @property
    def neighbors(self, node: Node) -> NeighboorDict:
        """Returns the list of neighbors of a node.
        """
        if node not in self._nodes_dict:
            raise ValueError("Node not in graph")
        return self._nodes_dict[node]

    @property
    def directed(self) -> bool:
        """Returns True if the graph is directed.
        """
        return self._directed

    @property
    def multigraph(self) -> bool:
        """Returns True if the graph is a multigraph.
        """
        return self._multigraph

    @property
    def num_nodes(self) -> int:
        """Returns the number of nodes of the graph.
        """
        return len(self._nodes_dict)

    @property
    def num_edges(self) -> int:
        """Returns the number of edges of the graph.
        """
        return len(self._edges_dict)

    @property
    def size(self) -> tuple:
        """Returns the number of edges of the graph.
        """
        return (self.num_nodes, self.num_edges)

    def is_multigraph(self) -> bool:
        """Returns True if the graph is a multigraph.
        """
        return self._multigraph

    def turn_into_multigraph(self) -> None:
        """Converts the graph into a multigraph.
        """
        self._multigraph = True

    def is_neighbor(self, node1: Node, node2: Node) -> bool:
        """Returns True if node2 is a neighbor of node1.
        """
        if node1 not in self._nodes_dict or node2 not in self._nodes_dict:
            raise ValueError("Not neighbors, one node"
                             "or both nodes is not in graph")
        return node2 in self._nodes_dict[node1]

    def is_edge(self, node1: Node, node2: Node) -> bool:
        """Returns True if node2 is a neighbor of node1.
        """
        if node1 not in self._nodes_dict:
            raise ValueError("Node not in graph")
        return (node1, node2) in self._edges_dict

    def nodes_list(self) -> list:
        """Returns the list of nodes of the graph.
        """
        return list(self._nodes_dict.keys())

    def edges_list(self) -> list:
        """Returns the list of edges of the graph.
        """
        return list(self._edges_dict.keys())

    def neighbors_list(self, node: Node) -> list:
        """Returns the list of neighbors of a node.
        """
        return list(self._nodes_dict[node].keys())

    def random_node(self, seed_value) -> Node:
        """Returns a random node of the graph.
        """
        seed(seed_value)
        return choice(self.nodes_list())

    def random_edge(self, seed_value) -> Edge:
        """Returns a random edge of the graph.
        """
        seed(seed_value)
        return choice(self.edges_list())

    def degree(self, node: Node) -> Union[int, tuple]:
        """Returns the degree of a node.
        """
        if node not in self._nodes_dict:
            raise ValueError("Node not in graph")
        if self._multigraph:
            return sum(self._nodes_dict[node].values())
        else:
            return len(self._nodes_dict[node])

    def add_node(self, node: Node) -> None:
        """Adds a node to the graph.
        """
        if node not in self._nodes_dict:
            self._nodes_dict[node] = {}
        else:
            raise ValueError("Node already in graph")

    def delete_node(self, node: Node) -> None:
        """Deletes a node from the graph.
        """
        if node not in self._nodes_dict:
            return

        # Deletes the node from neighbors and edges with the node
        for neighbor in self._nodes_dict[node]:
            if (neighbor in self._nodes_dict
                    and node in self._nodes_dict[neighbor]):
                del self._nodes_dict[neighbor][node]
            edge_to_delete = (node, neighbor)
            if edge_to_delete in self._edges_dict:
                del self._edges_dict[edge_to_delete]
            if not self._directed:
                edge_to_delete = (neighbor, node)
                if edge_to_delete in self._edges_dict:
                    del self._edges_dict[edge_to_delete]

        # Deletes node
        del self._nodes_dict[node]

    def add_edge(self, node1: Node, node2: Node) -> None:
        """Adds an edge to the graph. Behaves differently depending if the
        graph is multi or simple, and directed or undirected.
        """
        # Ensure nodes exist in the graph
        for node in [node1, node2]:
            if node not in self:
                self.add_node(node)

        # Canonicalize edge for undirected graphs
        if not self._directed:
            edge = tuple(sorted([node1, node2]))

        # Update the graph
        if self._multigraph or edge not in self:
            # Add or update the edge
            self._edges_dict[edge] = self._edges_dict.get(edge, 0) + 1
            self._nodes_dict[edge[0]][edge[1]] = (
                self._nodes_dict[edge[0]].get(edge[1], 0) + 1
            )
            # Update the neighbors of the nodes
            if not self._directed:
                self._nodes_dict[edge[1]][edge[0]] = (
                    self._nodes_dict[edge[1]].get(edge[0], 0) + 1
                )
            self._nodes_dict[edge[0]][edge[1]] = (
                self._nodes_dict[edge[0]].get(edge[1], 0) + 1
            )

    def _which_edge(self, edge):
        if edge in self._edges_dict:
            return edge
        elif self._is_inverse_edge(edge) in self._edges_dict:
            return self._is_inverse_edge(edge)
        else:
            raise ValueError("Edge not in graph")

    def delete_edge(self, edge: Edge) -> None:
        """Deletes an edge from the graph.
        """
        if edge not in self._edges_dict:
            raise ValueError("Edge not in graph")

        inverse_edge = self._invert_edge(edge)

        if not self._multigraph:
            del self._edges_dict[edge]
            if not self._directed and inverse_edge in self._edges_dict:
                del self._edges_dict[inverse_edge]
        else:
            self._nodes_dict[edge[0]][edge[1]] -= 1
            if not self._directed and inverse_edge in self._edges_dict:
                self._nodes_dict[edge[1]][edge[0]] -= 1

    def delete_all_parallel_edges(self, edge: Edge) -> None:
        """Deletes all parallel edges from the graph.
        """
        if edge not in self._edges_dict:
            raise ValueError("Edge not in graph")

        inverse_edge = self._invert_edge(edge)

        del self._edges_dict[edge]

        if not self._directed and inverse_edge in self._edges_dict:
            del self._edges_dict[inverse_edge]

    def contract_nodes(self, node1: Node, node2: Node) -> None:
        """Contracts two nodes of the graph into a supernode preserving
        the name of node1 and deleting node2. The nodes must be neighbors.
        Preserves the multigraph property of the graph and deletes loops,
        and new loops that may be created.
        """
        # Ensure nodes exist in the graph
        if node1 not in self or node2 not in self:
            raise ValueError("Node/s not in graph")
        if (node2 not in self[node1]
                and node1 not in self[node2]):
            raise ValueError("Nodes are not neighbors")

        # If the nodes are the same only gets rid of self loops and return
        if node1 == node2:
            self.delete_self_loops(node1)
            return

        # Unify the nodes and update the edges dictionary
        for neighbor in self[node2]:
            if neighbor != node1:
                # Creates the new edge
                if self._directed:
                    edge = (node1, neighbor)
                else:
                    # Canonicalize edge for undirected graphs
                    edge = tuple(sorted([node1, neighbor]))

                # Creates source edge
                if self._directed:
                    source_edge = (node2, neighbor)
                else:
                    # Canonicalize edge for undirected graphs
                    source_edge = tuple(sorted([node2, neighbor]))

                # Add or update the edge
                self._edges_dict[edge] = (
                    self._edges_dict.get(edge, 0)
                    + self._edges_dict.get(source_edge, 0)
                )
                if self._directed:
                    self._edges_dict[edge] = (
                        self._edges_dict.get(edge, 0)
                        + self._edges_dict.get(
                            self._invert_edge(source_edge), 0
                        )
                    )

                # Update the neighbor in node1 neighbor dictionary
                self._nodes_dict[node1][neighbor] = (
                    self._nodes_dict[node1].get(neighbor, 0)
                    + self._nodes_dict[node2].get(neighbor, 0)
                )

                # Update the neighbor if the graph is undirected
                if (not self._directed and neighbor != node1
                        and neighbor in self._nodes_dict):
                    self._nodes_dict[neighbor][node1] = (
                        self._nodes_dict[neighbor].get(node1, 0)
                        + self._nodes_dict[neighbor].get(node2, 0)
                    )

        # Assemble the old edge
        if self._directed:
            old_edge = (node1, node2)
        else:
            # Canonicalize edge for undirected graphs
            old_edge = tuple(sorted([node1, node2]))

        # Deletes the old edge
        self.delete_all_parallel_edges(old_edge)

        # Delete node2, its neighbors and its instances as a neighbor
        self.delete_node(node2)

    def delete_self_loops(self, node: Node) -> None:
        """Deletes all the self loops of a node.
        """
        if node not in self:
            raise ValueError("Node not in graph")
        if node in self[node]:
            del self._nodes_dict[node][node]
        self_edge = (node, node)
        if self_edge in self._edges_dict:
            del self._edges_dict[self_edge]

    @classmethod
    def copy(cls, graph: "Graph"):
        """Returns a deep copy of the graph.
        """
        graph_copy = cls(graph._directed, graph._multigraph)
        graph_copy._nodes_dict = copy.deepcopy(graph._nodes_dict)
        graph_copy._edges_dict = copy.deepcopy(graph._edges_dict)
        return graph_copy

    @classmethod
    def from_file(cls, file_name: str = None,
                  node_type: Node = int,
                  directed: bool = False,
                  multigraph: bool = False) -> "Graph":
        """Creates a graph from a file.

        The file muts contain the adjacency list representation of graph that
        can be simple or multigraph, and directed or undirected. The nodes
        must be either strings or integers. The first column represents
        the node label, and the rest of the row (other entries except
        the first column) tells all the nodes that are adjacent.

        For example, the row 1 2 3 4 means that the node 1 is adjacent
        to the nodes 2, 3 and 4.
        """
        graph = cls(directed, multigraph)
        with open(file_name) as f:
            for line in f:
                # Trim the line and skip if it's empty or starts with a comment
                line = line.strip()
                if not line or line.startswith('"""'):
                    continue

                # Split and process the line
                line_parts = line.split()
                node = node_type(line_parts[0])
                for neighbor in line_parts[1:]:
                    graph.add_edge(node, node_type(neighbor))

        return graph

    def _is_node(self, obj) -> bool:
        return isinstance(obj, (str, int))

    def _is_edge(self, obj) -> bool:
        return (isinstance(obj, tuple)
                and len(obj) == 2
                and self._is_node(obj[0])
                and self._is_node(obj[1]))

    def _is_neighboordict(self, obj) -> bool:
        return (isinstance(obj, dict)
                and all(self._is_node(k)
                        and isinstance(v, int) for k, v in obj.items()))

    def _is_nodedict(self, obj) -> bool:
        return (isinstance(obj, dict)
                and all(self._is_node(k)
                        and self._is_neighboordict(v) for k, v in obj.items()))

    def _is_edgedict(self, obj) -> bool:
        return (isinstance(obj, dict)
                and all(self._is_edge(k)
                        and isinstance(v, int) for k, v in obj.items()))

    def _is_elementdict(self, obj) -> bool:
        return self._is_nodedict(obj) or self._is_edgedict(obj)

    def _is_elementvalue(self, obj) -> bool:
        return self._is_neighboordict(obj) or isinstance(obj, int)
