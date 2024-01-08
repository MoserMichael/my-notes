# 787. Cheapest Flights Within K Stops
# Medium
#
#    There are n cities connected by some number of flights. You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.
#
#    You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.
#
#
#
#    Example 1:
#
#    Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
#    Output: 700
#    Explanation:
#    The graph is shown above.
#    The optimal path with at most 1 stop from city 0 to 3 is marked in red and has cost 100 + 600 = 700.
#    Note that the path through cities [0,1,2,3] is cheaper but is invalid because it uses 2 stops.
#
#    Example 2:
#
#    Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
#    Output: 200
#    Explanation:
#    The graph is shown above.
#    The optimal path with at most 1 stop from city 0 to 2 is marked in red and has cost 100 + 100 = 200.
#
#    Example 3:
#
#    Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0
#    Output: 500
#    Explanation:
#    The graph is shown above.
#    The optimal path with no stops from city 0 to 2 is marked in red and has cost 500.
#
#
#
#    Constraints:
#
#        1 <= n <= 100
#        0 <= flights.length <= (n * (n - 1) / 2)
#        flights[i].length == 3
#        0 <= fromi, toi < n
#        fromi != toi
#        1 <= pricei <= 104
#        There will not be any multiple flights between two cities.
#        0 <= src, dst, k < n
#        src != dst
#
#

#
#    # Intuition
#
#    breadth first search, with memoization.
#    You keep a map that maps the node to an entry of the last best result.
#    if current result is worse then the last best result then don't continue with the traversal of the graph.
#
#    Now the memozation check that checks if the current result is worse than the previous one is tricky:
#     - the last best result is a pair of numbers ( <cost of last best result>, <current number of remaining steps at visit> )
#     - if the current traversal costs less than the last best result - continue with the traversal
#     - if the number of remaining steps is bigger then number of remaining steps of last big result - continue with the traversal (it might be, that this will give you the advantage of reaching the target node!)
#     Upon passing this check: set the memoization state:
#       - the first number of the entry is the minimum of the last best result and the current one
#       - the second number is set to the maximum of of the remaining step value for last best result and the current one.
#
#
#    # Approach
#    <!-- Describe your approach to solving the problem. -->
#
#    # Complexity
#    - Time complexity:
#    Works case may visit all edges and vertexes, so it is: $$O(V + E)$$
#
#    - Space complexity:
#    keep an entry for each vertex $$O(V)$$
#



import math

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        self.minDistMap = {}

        self.visited = set()
        self.target = dst
        self.minPathCost = math.inf
        self.graph = Solution.buildGraph(flights)

        self.rec(src, 0, k)


        if self.minPathCost == math.inf:
            return -1
        return self.minPathCost

    def buildGraph(flights):
        graph = {}
        for f in flights:
            entry = graph.setdefault(f[0], [])
            entry.append( (f[1], f[2]) )
        return graph

    def rec(self, curNode, pathCost, steps):

        if curNode in self.visited:
            return

        if curNode not in self.minDistMap:
            self.minDistMap[curNode] = (pathCost, steps)
        else:
            last = self.minDistMap[curNode]

            if last[0] > pathCost or last[1] < steps: # or last[1] == -1:
                self.minDistMap[curNode] = (min(last[0], pathCost), max(last[1],steps) )
            else:
                return

        if curNode == self.target:
            #print(f"-> {pathCost}")
            self.minPathCost = min(self.minPathCost, pathCost)
            return


        if steps >= 0:
            edges = self.graph.get(curNode)
            if edges:
                self.visited.add(curNode)
                for e in edges:
                    self.rec(e[0], pathCost+e[1], steps-1)
                self.visited.remove(curNode)



