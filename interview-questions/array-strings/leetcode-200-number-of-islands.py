# 200. Number of Islands
# Medium
#    Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
#
#    An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
#
#
#
#    Example 1:
#
#    Input: grid = [
#      ["1","1","1","1","0"],
#      ["1","1","0","1","0"],
#      ["1","1","0","0","0"],
#      ["0","0","0","0","0"]
#    ]
#    Output: 1
#
#    Example 2:
#
#    Input: grid = [
#      ["1","1","0","0","0"],
#      ["1","1","0","0","0"],
#      ["0","0","1","0","0"],
#      ["0","0","0","1","1"]
#    ]
#    Output: 3
#
#
#
#    Constraints:
#
#        m == grid.length
#        n == grid[i].length
#        1 <= m, n <= 300
#        grid[i][j] is '0' or '1'.
#
#


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        dy = len(grid)
        dx = len(grid[0])

        def paint_it(x, y):
            nonlocal dx, dy, grid

            if 0<=x<dx and 0<=y<dy and grid[y][x]=="1":
                grid[y][x] = "2"
                paint_it(x-1,y)
                paint_it(x+1,y)
                paint_it(x,y+1)
                paint_it(x,y-1)

        dy = len(grid)
        dx = len(grid[0])

        count = 0

        for idx_y in range(dy):
            for idx_x in range(dx):
                if grid[idx_y][idx_x] == "1":
                    count += 1
                    paint_it(idx_x, idx_y)

        return count
