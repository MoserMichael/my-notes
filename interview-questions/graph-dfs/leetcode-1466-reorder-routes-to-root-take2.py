# 1466. Reorder Routes to Make All Paths Lead to the City Zero
# Medium
#There are n cities numbered from 0 to n - 1 and n - 1 roads such that there is only one way to travel between two different cities (this network form a tree). Last year, The ministry of transport decided to orient the roads in one direction because they are too narrow.
#
#Roads are represented by connections where connections[i] = [ai, bi] represents a road from city ai to city bi.
#
#This year, there will be a big event in the capital (city 0), and many people want to travel to this city.
#
#Your task consists of reorienting some roads such that each city can visit the city 0. Return the minimum number of edges changed.
#
#It's guaranteed that each city can reach city 0 after reorder.
#
# 
#
#Example 1:
#
#Input: n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
#Output: 3
#Explanation: Change the direction of edges show in red such that each node can reach the node 0 (capital).
#
#Example 2:
#
#Input: n = 5, connections = [[1,0],[1,2],[3,2],[3,4]]
#Output: 2
#Explanation: Change the direction of edges show in red such that each node can reach the node 0 (capital).
#
#Example 3:
#
#Input: n = 3, connections = [[1,0],[2,0]]
#Output: 0
#
# 
#
#Constraints:
#
#    2 <= n <= 5 * 104
#    connections.length == n - 1

class Solution:
    def minReorder(self, n: int, edges: List[List[int]]) -> int:

        graph, insertedEdges = Solution.makeGraph(n, edges)

        setOfWalkedEdges = set()
        visitedNodes=set()

        Solution.walk(0, graph, setOfWalkedEdges, visitedNodes)
        assert(len(setOfWalkedEdges) == n - 1)

        ret = Solution.removeOtherEdges(graph, setOfWalkedEdges, insertedEdges)
        return ret

    @staticmethod
    def makeGraph(n, edges):
        insertedEdges = set()

        graph = []
        for idx in range(0, n):
            graph.append( set() )
        for edge in edges:
            graph[edge[0]].add(edge[1])
            graph[edge[1]].add(edge[0])
            insertedEdges.add( (edge[1], edge[0]) )

        return graph, insertedEdges

    
    @staticmethod
    def walk(node, graph, setOfWalkedEdges, visitedNodes):

        if node in visitedNodes:
            return False
        visitedNodes.add(node)    

        conn = graph[node]
        for idxTo in conn:            
            if Solution.walk(idxTo, graph, setOfWalkedEdges, visitedNodes):
                    edge=(node,idxTo)
                    setOfWalkedEdges.add(edge)


        return True

    @staticmethod
    def removeOtherEdges(graph, setOfWalkedEdges, insertedEdges):

        changedEdges = len(insertedEdges)

        for edge in setOfWalkedEdges:
            if edge in insertedEdges:
                changedEdges -= 1
        
        return changedEdges
                

