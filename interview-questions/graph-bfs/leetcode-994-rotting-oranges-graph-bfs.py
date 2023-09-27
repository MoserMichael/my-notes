# 994. Rotting Oranges
# Medium
#You are given an m x n grid where each cell can have one of three values:
#
#    0 representing an empty cell,
#    1 representing a fresh orange, or
#    2 representing a rotten orange.
#
#Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
#
#Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
#
#
#
#Example 1:
#
#Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
#Output: 4
#
#Example 2:
#
#Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
#Output: -1
#Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
#
#Example 3:
#
#Input: grid = [[0,2]]
#Output: 0
#Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
#
#
#
#Constraints:
#
#    m == grid.length
#    n == grid[i].length
#    1 <= m, n <= 10
#    grid[i][j] is 0, 1, or 2.
#
#


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        posBadList = []
        orangesCount = Solution.countOranges(grid, posBadList)
        #print(f"orangesCount {orangesCount} posBad {posBadList}")

        visitedSet=set(posBadList)

        return Solution.simulateR(grid, posBadList, visitedSet, orangesCount, 0)

    @staticmethod
    def simulateR(grid, posBadList, visitedSet, orangesCount, stepPassed):


        #print(f"posBad {posBadList} visitedSet {visitedSet} stepPassed {stepPassed}")

        if len(visitedSet) == orangesCount:
            return stepPassed

        nextBadPos = []

        for pos in posBadList:
            for nextPos in Solution.adjacentList(pos,grid):
                if nextPos not in visitedSet:
                    visitedSet.add(nextPos)
                    nextBadPos.append(nextPos)


        if len(nextBadPos) == 0:
            return -1

        return Solution.simulateR(grid, nextBadPos, visitedSet, orangesCount, stepPassed + 1)




    @staticmethod
    def adjacentList(pos, grid):
        posMove = [ (-1,0), (1,0), (0,-1), (0,1)]
        ret = []
        for dpos in posMove:
            nextY = pos[0]+dpos[0]
            nextX = pos[1]+dpos[1]

            if 0 <= nextY < len(grid) and 0 <= nextX < len(grid[0]):

                if grid[nextY][nextX] == 1:

                    ret.append((nextY, nextX))

        #print(f"adjacentList pos {pos} -> {ret}")
        return ret


    @staticmethod
    def countOranges(grid, posBadList):
        count = 0

        for yIdx in range(0, len(grid)):
            for xIdx in range(0,len(grid[yIdx])):
                if grid[yIdx][xIdx] != 0:
                    count += 1
                if grid[yIdx][xIdx] == 2:
                    posBadList.append( (yIdx, xIdx))

        return count
