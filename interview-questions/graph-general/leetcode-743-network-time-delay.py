# 743. Network Delay Time
# Medium
#
#    You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.
#
#    We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.
#
#
#
#    Example 1:
#
#    Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
#    Output: 2
#
#    Example 2:
#
#    Input: times = [[1,2,1]], n = 2, k = 1
#    Output: 1
#
#    Example 3:
#
#    Input: times = [[1,2,1]], n = 2, k = 2
#    Output: -1
#
#
#
#    Constraints:
#
#        1 <= k <= n <= 100
#        1 <= times.length <= 6000
#        times[i].length == 3
#        1 <= ui, vi <= n
#        ui != vi
#        0 <= wi <= 100
#        All the pairs (ui, vi) are unique. (i.e., no multiple edges.)
#

import math
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph, remainingSet = Solution.buildGraph(times, n, k)


        # doing Dijkstra's shortest path.
        mapNodeToCost={ (k-1) : 0 }

        currentNode = k
        costHeap = []
        heapq.heapify(costHeap)

        while len(remainingSet) != 0:
            path_cost = mapNodeToCost[currentNode-1]

            for adj in graph[currentNode-1]:
                target = adj[0]
                cost = path_cost + adj[1]

                if cost < mapNodeToCost.setdefault(target-1, math.inf):
                    mapNodeToCost[target-1] = cost

                heapq.heappush(costHeap, (cost, target) )

            if len(costHeap) == 0:
                break

            currentNode = -1
            # find next cheapest
            while len(costHeap) != 0:
                e = heapq.heappop(costHeap)
                node = e[1]
                if node-1 in remainingSet:
                    remainingSet.remove(node-1)
                    currentNode = node
                    break

            if currentNode == -1:
                break

        # eof loop
        if len(mapNodeToCost) < n:
            return -1

        # find max path value computed
        return reduce(lambda prev, elm: max(prev, elm), mapNodeToCost.values(), 0)



    def buildGraph(times, n, initNode):
        graph = [ [].copy() for i in range(0, n) ]
        for e in times:
            graph[ e[0]-1 ].append( (e[1], e[2]) )

        remainingSet = set()
        for idx in range(0,n):
            if idx != initNode-1:
                remainingSet.add(idx)

        return graph, remainingSet


