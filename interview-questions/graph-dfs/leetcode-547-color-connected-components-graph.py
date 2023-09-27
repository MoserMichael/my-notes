#547. Number of Provinces
# Medium
#There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.
#
#A province is a group of directly or indirectly connected cities and no other cities outside of the group.
#
#You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.
#
#Return the total number of provinces.
#
#
#
#Example 1:
#
#Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
#Output: 2
#
#Example 2:
#
#Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
#Output: 3
#
#
#
#Constraints:
#
#    1 <= n <= 200
#    n == isConnected.length
#    n == isConnected[i].length
#    isConnected[i][j] is 1 or 0.
#    isConnected[i][i] == 1
#    isConnected[i][j] == isConnected[j][i]
#

class Solution:
    def findCircleNum(self, graph: List[List[int]]) -> int:
        visitedMap={}
        maxColor = 0

        for nodeIdx in range(0, len(graph)):
            maxColor = Solution.imp(graph, nodeIdx, maxColor, visitedMap)
            #print(f"idx: {nodeIdx} color: {visitedMap}")

        return maxColor

    @staticmethod
    def imp(graph, node, maxColor, visitedMap):
        if node in visitedMap:
            return maxColor

        # connected to a known connected component?
        connections = graph[node]
        for linkIdx in range(0, len(connections)):
            if connections[linkIdx] and linkIdx in visitedMap:
                visitedMap[node] = visitedMap[linkIdx]
                return maxColor


        maxColor += 1

        Solution.colorIt(graph, node, maxColor, visitedMap)

        return maxColor

    @staticmethod
    def colorIt(graph, node, maxColor, visitedMap):

        visitedMap[node] = maxColor

        connections = graph[node]
        for idx in range(0, len(connections)):
            if connections[idx] and idx not in visitedMap:
                Solution.colorIt(graph, idx, maxColor, visitedMap)

