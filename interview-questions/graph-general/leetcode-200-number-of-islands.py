# 200. Number of Islands
# Medium
#Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
#
#An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
#
# 
#
#Example 1:
#
#Input: grid = [
#  ["1","1","1","1","0"],
#  ["1","1","0","1","0"],
#  ["1","1","0","0","0"],
#  ["0","0","0","0","0"]
#]
#Output: 1
#
#Example 2:
#
#Input: grid = [
#  ["1","1","0","0","0"],
#  ["1","1","0","0","0"],
#  ["0","0","1","0","0"],
#  ["0","0","0","1","1"]
#]
#Output: 3
#
# 
#
#Constraints:
#
#    m == grid.length
#    n == grid[i].length
#    1 <= m, n <= 300
#    grid[i][j] is '0' or '1'.
#


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        visitedNodeMap = {}

        nextColor = 0
        for posx in range(0, len(grid[0])):
            for posy in range(0, len(grid)):
                if grid[posy][posx] == "1":
                    currentPos = (posx, posy)
                    if currentPos not in visitedNodeMap:
                        nextColor+= 1
                        #print(f"color {nextColor} pos: {currentPos}")
                        Solution.walkGraphDFS(currentPos, grid, visitedNodeMap, nextColor)

        return nextColor


    # can be done as both BFS and DFS
    # for board of infinite size you must do BFS (otherwise the recursion falls through)

    @staticmethod
    def walkGraphDFS( nodePos, grid, visitedNodeMap, nextColor):
        if nodePos in visitedNodeMap:
            assert visitedNodeMap[nodePos] == nextColor
            return
        visitedNodeMap[nodePos] = nextColor

        for node in Solution.getAdjacentNodes(nodePos, grid):
            Solution.walkGraphDFS(node, grid, visitedNodeMap, nextColor)

    def getAdjacentNodes(nodePos, grid):
        deltas=[(-1,0),(1,0),(0,-1),(0,1)]

        ret = []
        for delta in deltas:
            posx = nodePos[0]+delta[0]
            posy = nodePos[1]+delta[1]

            if 0<=posx<len(grid[0]) and 0<=posy<len(grid):
                if grid[posy][posx] == "1":
                    ret.append((posx,posy))

        return ret


