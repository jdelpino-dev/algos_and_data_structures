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
