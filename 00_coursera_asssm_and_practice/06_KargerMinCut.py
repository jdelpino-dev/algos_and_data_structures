from graph1 import Graph
from random import randint


def repeat_karger_min_cuts(original_graph: Graph, times: int) -> int:
    """
    Return the minimum number of cuts in a graph.
    """
    min_cuts = float("inf")

    for _ in range(times):
        seed = randint(99, 6_0043_110)
        contraction_graph = Graph.copy(original_graph)
        contraction_graph.turn_into_multigraph()
        cuts = karger_min_cuts(contraction_graph, seed)
        if cuts < min_cuts:
            min_cuts = cuts
        # print(f"Current min cuts: {min_cuts}")

    return min_cuts, contraction_graph.size


def karger_min_cuts(contraction_graph: Graph, seed_value) -> int:
    """
    Return the minimum number of cuts in a graph.
    """

    # Contract the graph until there are only two nodes left.
    while (len(contraction_graph.nodes) > 2
           and len(contraction_graph.edges) > 0):
        edge = contraction_graph.random_edge(seed_value=seed_value)
        contraction_graph.contract_nodes(*edge)
        contraction_graph.delete_self_loops(edge[0])
    # print(f"Graph size: {contraction_graph.size}")
    # print(f"Graph nodes: {contraction_graph.nodes}")
    # print(f"Graph edges: {contraction_graph.edges}")

    # Get one of the two remaining nodes.
    # graphnodes = list(contraction_graph.nodes)
    # node = graphnodes[0]
    # Return the number of edges between the two remaining nodes.
    # return contraction_graph.degree(node)
    supernode = contraction_graph.edges_list()[0]
    return contraction_graph[supernode]


# Main block
if __name__ == "__main__":
    # filename = (
    #     "./20_algos_and_data_structures/00_coursera_asssm_and_practice"
    #     "/05_data/graph_1.txt"
    # )
    # filename = ("./00_coursera_asssm_and_practice"
    #             "/05_data/graph_1.txt")
    # filename = ("00_coursera_asssm_and_practice"
    #             "/05_data/graph_1.txt")
    # filename = "05_data/graph_1.txt"
    # filename = "./05_data/graph_1.txt"
    filename = ("/Users/jdelpino/Library/Mobile Documents/"
                "com~apple~CloudDocs/Docus-Nube/SWE & AI/code_workspaces/"
                "swe-proyects/springboard_code/20_algos_and_data_structures/"
                "00_coursera_asssm_and_practice/05_data/graph_1.txt")

    graph = Graph.from_file(filename,
                            node_type=int,
                            directed=False,
                            multigraph=False)
    print(graph.size)

    # print(repeat_karger_min_cuts(graph, 306000))
    # print(repeat_karger_min_cuts(graph, 1500))
    print(repeat_karger_min_cuts(graph, 200))
