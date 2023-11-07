# 64. Minimum Path Sum
# Medium
#    Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.
#
#    Note: You can only move either down or right at any point in time.
#
#
#
#    Example 1:
#
#    Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
#    Output: 7
#    Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
#
#    Example 2:
#
#    Input: grid = [[1,2,3],[4,5,6]]
#    Output: 12
#
#
#
#    Constraints:
#
#        m == grid.length
#        n == grid[i].length
#        1 <= m, n <= 200
#        0 <= grid[i][j] <= 200
#

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        return Solution.rec(grid)

    def rec(grid):
        row = [0] * len(grid[0])
        memo_tbl = [ row.copy() for idx in range(0,len(grid)) ]

        Solution.recur(0, 0, grid, memo_tbl)

        #for r in memo_tbl:
        #    print(r)

        return memo_tbl[0][0]

    def recur(x, y, grid, memo_tbl):

        if memo_tbl[y][x] != 0:
            return memo_tbl[y][x]

        next_x = x+1
        next_y = y+1

        val_x = val_y = -1

        if next_x < len(grid[0]):
            val_x = Solution.recur(next_x, y, grid, memo_tbl)
        if next_y < len(grid):
            val_y = Solution.recur(x, next_y, grid, memo_tbl)

        if val_x == -1 and val_y == -1:
            memo_tbl[y][x] = grid[y][x]
        elif val_x == -1:
            memo_tbl[y][x] = grid[y][x] + val_y
        elif val_y == -1:
            memo_tbl[y][x] = grid[y][x] + val_x
        else:
            memo_tbl[y][x] = grid[y][x] + min(val_x, val_y)

        return memo_tbl[y][x]

