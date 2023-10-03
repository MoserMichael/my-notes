# 207. Course Schedule
# Medium
#There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
#
#    For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
#
#Return true if you can finish all courses. Otherwise, return false.
#
#
#
#Example 1:
#
#Input: numCourses = 2, prerequisites = [[1,0]]
#Output: true
#Explanation: There are a total of 2 courses to take.
#To take course 1 you should have finished course 0. So it is possible.
#
#Example 2:
#
#Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
#Output: false
#Explanation: There are a total of 2 courses to take.
#To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
#
#
#
#Constraints:
#
#    1 <= numCourses <= 2000
#    0 <= prerequisites.length <= 5000
#    prerequisites[i].length == 2
#    0 <= ai, bi < numCourses
#    All the pairs prerequisites[i] are unique.
#

class Solution:

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = Solution.buildGraph(numCourses, prerequisites)
        all_visited_nodes = set()

        for idx in range(0, numCourses-1):
            ret, num_visited = Solution.walkGraph(idx, graph, set(), all_visited_nodes)
            if ret:
                return False
            if num_visited == numCourses:
                return True
        return True

    @staticmethod
    def buildGraph(numCourses, prerequisites):
        graph = [None] * numCourses

        for prereq in prerequisites:
            from_node = prereq[1]
            to_node = prereq[0]

            if graph[from_node] is None:
                graph[from_node] = []

            graph[from_node].append(to_node)

        #print(f"graph: {graph}")
        return graph

    @staticmethod
    def walkGraph(node_idx, graph, visited_nodes, all_visited_nodes):
        if node_idx in visited_nodes:
            return True, 0

        if node_idx in all_visited_nodes:
            return False, 0

        visited = 1
        visited_nodes.add(node_idx)
        all_visited_nodes.add(node_idx)

        linked_nodex = graph[node_idx]
        ret = False
        if linked_nodex:
            for linked_node in linked_nodex:
                ret, nvisited = Solution.walkGraph(linked_node, graph, visited_nodes, all_visited_nodes)
                if ret:
                    break
                visited += nvisited
        visited_nodes.remove(node_idx)

        return ret, visited






