# 695. Max Area of Island
# Medium
#
#    You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.
#
#    The area of an island is the number of cells with a value 1 in the island.
#
#    Return the maximum area of an island in grid. If there is no island, return 0.
#
#
#
#    Example 1:
#
#    Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
#    Output: 6
#    Explanation: The answer is not 11, because the island must be connected 4-directionally.
#
#    Example 2:
#
#    Input: grid = [[0,0,0,0,0,0,0,0]]
#    Output: 0
#
#
#
#    Constraints:
#
#        m == grid.length
#        n == grid[i].length
#        1 <= m, n <= 50
#        grid[i][j] is either 0 or 1.
#
#



class Solution:

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        r = 0
        for idx_y in range(0, len(grid)):
            for idx_x in range(0,len(grid[0])):
                if grid[idx_y][idx_x] == 1:
                    r = max(r, Solution.paintIsland(grid, idx_y, idx_x))

        return r

    def paintIsland(grid, y, x):
        if  y<0 or y>=len(grid) or x<0 or x >=len(grid[0]):
            return 0

        if grid[y][x] <= 0:
            return 0
        grid[y][x] = -1

        return 1 + Solution.paintIsland(grid, y-1, x) + Solution.paintIsland(grid, y+1, x) + Solution.paintIsland(grid, y, x-1) + Solution.paintIsland(grid, y, x+1)

