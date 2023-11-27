# 802. Find Eventual Safe States
# Medium
#
#    There is a directed graph of n nodes with each node labeled from 0 to n - 1. The graph is represented by a 0-indexed 2D integer array graph where graph[i] is an integer array of nodes adjacent to node i, meaning there is an edge from node i to each node in graph[i].
#
#    A node is a terminal node if there are no outgoing edges. A node is a safe node if every possible path starting from that node leads to a terminal node (or another safe node).
#
#    Return an array containing all the safe nodes of the graph. The answer should be sorted in ascending order.
#
#
#
#    Example 1:
#    Illustration of graph
#
#    Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
#    Output: [2,4,5,6]
#    Explanation: The given graph is shown above.
#    Nodes 5 and 6 are terminal nodes as there are no outgoing edges from either of them.
#    Every path starting at nodes 2, 4, 5, and 6 all lead to either node 5 or 6.
#
#    Example 2:
#
#    Input: graph = [[1,2,3,4],[1,2],[3,4],[0,4],[]]
#    Output: [4]
#    Explanation:
#    Only node 4 is a terminal node, and every path starting at node 4 leads to node 4.
#
#
#
#    Constraints:
#
#        n == graph.length
#        1 <= n <= 104
#        0 <= graph[i].length <= n
#        0 <= graph[i][j] <= n - 1
#        graph[i] is sorted in a strictly increasing order.
#        The graph may contain self-loops.
#        The number of edges in the graph will be in the range [1, 4 * 104].
#
#


# Python3, not very fast, with lots of explanations
#    # Intuition
#    - conversion of the input to an adjacency graph, that keeps both forward and backward edges.
#    - mark all nodes without outgoing edges as 'safe nodes' (maintain a set of safe nodes)
#    - compute the closure of all 'safe nodes'. Closure means that you have a loop that tries to to increment the size of the set of 'safe nodes'. Continue while it has been able to increment the set of 'safe nodes' - it it didn't manage to increment this set then break out of the loop.
#    - How do we try to incrmeent the size of 'save nodes' - start with the known set of 'safe nodes'. Follow the backlinks to the nodes that point to this set. for each of these candidates: check if all its links point to 'safe nodes'. If this is the case then add the node to the set of 'safe nodes'. Maintain a counter of nodes that were added to the set of 'save nodes'.
#
#    - when all this is done; convert the set of 'save nodes' to a list. sort it by the number of the nodes (that's one of the peculiar conditions of this task)
#    - return the result.
#
#    # Complexity
#    - Time complexity:
#    The worst case would be O(n^2) where n is the number of nodes in the graph.
#


class Node:
    def __init__(self, num):
        self.num = num
        self.outgoing_edges = []
        self.back_edges = []

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:

        gr = Solution.buildGraph(graph)

        safe_nodes = set()

        # add terminal nodes to set of safe nodes
        for node in gr.values():
            if len(node.outgoing_edges) == 0:
                safe_nodes.add(node.num)


        # closure of the safe node
        # each iteration tries to extend the set of safe nodes
        # each iteration should add more safe nodes
        # if none were added then break
        while True:
            if Solution.addSafeNodes(gr, safe_nodes) == 0:
                break

        return sorted(safe_nodes)

        #ret = list(safe_nodes)
        #ret.sort()
        #return ret

    def addSafeNodes(graph, safe_nodes):
        added = 0
        for node in graph.values():
            if node.num in safe_nodes:
                added += Solution.rec(graph, node, safe_nodes)

        return added

    def rec(graph, node, safe_nodes):
        ret = 0

        #next_level = []

        for n in node.back_edges:
            # is n a safe node
            node_ref = graph[n]

            if node_ref.num in safe_nodes:
                continue

            all_safe_refs = True
            for o in node_ref.outgoing_edges:
                if not o in safe_nodes:
                    all_safe_refs = False
                    break

            if all_safe_refs:
                ret += 1
                safe_nodes.add(node_ref.num)
                ret += Solution.rec(graph, node_ref, safe_nodes)

                #next_level.append(node_ref)

        #for n in next_level:
        #    ret += Solution.rec(graph, n, safe_nodes)

        return ret

    def buildGraph(graph):
        gr = {}

        for k in range(0, len(graph)):
            gr[k] = Node(k)

        for k, edges in enumerate(graph):
            out = gr[k]
            for e in edges:
                out.outgoing_edges.append(e)
                gr[e].back_edges.append(k)


        #for k, edges in enumerate(graph):
        #    out = gr.setdefault(k, Node(k))
        #    for e in edges:
        #        out.outgoing_edges.append(e)
        #        oth = gr.setdefault(e, Node(e))
        #        oth.back_edges.append(k)

        return gr
