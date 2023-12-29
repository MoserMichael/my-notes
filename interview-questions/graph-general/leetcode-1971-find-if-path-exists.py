# 1971. Find if Path Exists in Graph
# Easy
#
#    There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive). The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.
#
#    You want to determine if there is a valid path that exists from vertex source to vertex destination.
#
#    Given edges and the integers n, source, and destination, return true if there is a valid path from source to destination, or false otherwise.
#
#
#
#    Example 1:
#
#    Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
#    Output: true
#    Explanation: There are two paths from vertex 0 to vertex 2:
#    - 0 → 1 → 2
#    - 0 → 2
#
#    Example 2:
#
#    Input: n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5
#    Output: false
#    Explanation: There is no path from vertex 0 to vertex 5.
#
#
#
#    Constraints:
#
#        1 <= n <= 2 * 105
#        0 <= edges.length <= 2 * 105
#        edges[i].length == 2
#        0 <= ui, vi <= n - 1
#        ui != vi
#        0 <= source, destination <= n - 1
#        There are no duplicate edges.
#        There are no self edges.
#



class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        # why? there is a path between source and destination, and the length of the path is zero?
        if source == destination:
            return True

        graph = Solution.buildGraph(edges)
        return Solution.walkBFS(graph, source, destination)

    def walkBFS(graph, source, destination):

        cur_nodes = [ source ]
        visited_nodes = set(cur_nodes)

        while len(cur_nodes) != 0:
            next_cur_nodes = []
            for node in cur_nodes:
                out_nodes = graph.get(node)
                if out_nodes:
                    for out_node in out_nodes:
                        if out_node not in visited_nodes:
                            if out_node == destination:
                                return True
                            visited_nodes.add(out_node)
                            next_cur_nodes.append(out_node)


            cur_nodes = next_cur_nodes

        return False


    def buildGraph(edges):
        map_nodes_to_edges = {}

        for edge in edges:

            con_nodes = map_nodes_to_edges.setdefault(edge[0], [] )
            con_nodes.append(edge[1])

            con_nodes = map_nodes_to_edges.setdefault(edge[1], [] )
            con_nodes.append(edge[0])


        return map_nodes_to_edges

