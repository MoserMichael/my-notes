# 1219. Path with Maximum Gold
# Medium
#
#    In a gold mine grid of size m x n, each cell in this mine has an integer representing the amount of gold in that cell, 0 if it is empty.
#
#    Return the maximum amount of gold you can collect under the conditions:
#
#        Every time you are located in a cell you will collect all the gold in that cell.
#        From your position, you can walk one step to the left, right, up, or down.
#        You can't visit the same cell more than once.
#        Never visit a cell with 0 gold.
#        You can start and stop collecting gold from any position in the grid that has some gold.
#
#
#
#    Example 1:
#
#    Input: grid = [[0,6,0],[5,8,7],[0,9,0]]
#    Output: 24
#    Explanation:
#    [[0,6,0],
#     [5,8,7],
#     [0,9,0]]
#    Path to get the maximum gold, 9 -> 8 -> 7.
#
#    Example 2:
#
#    Input: grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
#    Output: 28
#    Explanation:
#    [[1,0,7],
#     [2,0,6],
#     [3,4,5],
#     [0,3,0],
#     [9,0,20]]
#    Path to get the maximum gold, 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7.
#
#
#
#    Constraints:
#
#        m == grid.length
#        n == grid[i].length
#        1 <= m, n <= 15
#        0 <= grid[i][j] <= 100
#        There are at most 25 cells containing gold.
#


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        #return Solution.slowSolution(grid)
        return Solution.fastSolution(grid)

    def fastSolution(grid):
        def walk(x, y):
            nonlocal grid

            if not 0 <= x < len(grid[0]) or not 0 <= y < len(grid) or grid[y][x] == 0:
                return 0

            prev = grid[y][x]
            grid[y][x] = 0

            ret = prev + max( walk(x-1, y), walk(x+1, y), walk(x, y-1), walk(x, y+1))

            grid[y][x] = prev

            return ret

        ret = 0
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                ret = max(ret, walk(x, y))

        return ret

    def slowSolution(grid):
        def walk(x, y, visited):
            nonlocal grid

            if not 0 <= x < len(grid[0]) or not 0 <= y < len(grid):
                return 0

            if grid[y][x] == 0:
                return 0

            if (x, y) in visited:
                return 0

            visited.add( (x, y) )
            ret = grid[y][x] + max( walk(x-1, y, visited), walk(x+1, y, visited), walk(x, y-1, visited), walk(x, y+1, visited))
            visited.remove( (x, y) )
            return ret

        ret = 0
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                ret = max(ret, walk(x, y, set()))

        return ret
