# was too slow for very big graphs,
# need to rewrite, to use sparse graphs.
# bother!

class Solution:
    def minReorder(self, n: int, edges: List[List[int]]) -> int:

        graph = Solution.makeGraph(n, edges)
        insertedEdges = Solution.makeGraphBidi(graph)
        setOfWalkedEdges = set()
        visitedNodes=set()

        Solution.walk(0, graph, setOfWalkedEdges, visitedNodes)
        assert(len(setOfWalkedEdges) == n - 1)

        ret = Solution.removeOtherEdges(graph, setOfWalkedEdges, insertedEdges)
        return ret

    @staticmethod
    def makeGraph(n, edges):
        graph = []
        for idx in range(0, n):
            graph.append( [0] * n )
        for edge in edges:
            graph[edge[0]][edge[1]] = 1
        return graph

    @staticmethod
    def makeGraphBidi(graph):

        insertedEdges = set()

        for idx in range(0, len(graph)):
            conn = graph[idx]
            for idxTo in range(0,len(conn)):
                if graph[idx][idxTo]:
                    if not graph[idxTo][idx]:
                        graph[idxTo][idx] = 1
                        insertedEdges.add( (idxTo, idx))    
            
        return insertedEdges

    @staticmethod
    def walk(node, graph, setOfWalkedEdges, visitedNodes):

        if node in visitedNodes:
            return False
        visitedNodes.add(node)    

        conn = graph[node]
        for idxTo in range(0,len(conn)):
            if graph[node][idxTo]:
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
                

