# 463. Island Perimeter
# Easy
#
#    You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.
#
#    Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).
#
#    The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.
#
#
#
#    Example 1:
#
#    Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
#    Output: 16
#    Explanation: The perimeter is the 16 yellow stripes in the image above.
#
#    Example 2:
#
#    Input: grid = [[1]]
#    Output: 4
#
#    Example 3:
#
#    Input: grid = [[1,0]]
#    Output: 4
#
#
#
#    Constraints:
#
#        row == grid.length
#        col == grid[i].length
#        1 <= row, col <= 100
#        grid[i][j] is 0 or 1.
#        There is exactly one island in grid.
#



class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        dx = len(grid[0])
        dy = len(grid)
        visitedSet = set()

        def findLand(grid):
            for y in range(dy):
                for x in range(dx):
                    if grid[y][x]:
                        return y, x
            return -1, -1

        y, x = findLand(grid)
        if y == -1:
            return 0

        mov = [ (-1,0), (1,0), (0,-1), (0,1) ]

        def findPerimeter(y, x):
            if x < 0 or x >= dx or y < 0 or y >= dy:
                return 1

            if grid[y][x] == 0:
                return 1

            if (y, x) in visitedSet:
                return 0
            visitedSet.add( (y, x) )

            perim = 0
            for m in mov:
                perim += findPerimeter(y+m[0], x+m[1])

            return perim

        return findPerimeter(y, x)

