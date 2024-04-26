# 1289. Minimum Falling Path Sum II
# Hard
#
#    Given an n x n integer matrix grid, return the minimum sum of a falling path with non-zero shifts.
#
#    A falling path with non-zero shifts is a choice of exactly one element from each row of grid such that no two elements chosen in adjacent rows are in the same column.
#
#
#
#    Example 1:
#
#    Input: grid = [[1,2,3],[4,5,6],[7,8,9]]
#    Output: 13
#    Explanation:
#    The possible falling paths are:
#    [1,5,9], [1,5,7], [1,6,7], [1,6,8],
#    [2,4,8], [2,4,9], [2,6,7], [2,6,8],
#    [3,4,8], [3,4,9], [3,5,7], [3,5,9]
#    The falling path with the smallest sum is [1,5,7], so the answer is 13.
#
#    Example 2:
#
#    Input: grid = [[7]]
#    Output: 7
#
#
#
#    Constraints:
#
#        n == grid.length == grid[i].length
#        1 <= n <= 200
#        -99 <= grid[i][j] <= 99
#
#

#
#    Given an n x n integer matrix grid, return the minimum sum of a falling path with non-zero shifts.
#
#    A falling path with non-zero shifts is a choice of exactly one element from each row of grid such that no two elements chosen in adjacent rows are in the same column.
#
#
#
#    Example 1:
#
#    Input: grid = [[1,2,3],[4,5,6],[7,8,9]]
#    Output: 13
#    Explanation:
#    The possible falling paths are:
#    [1,5,9], [1,5,7], [1,6,7], [1,6,8],
#    [2,4,8], [2,4,9], [2,6,7], [2,6,8],
#    [3,4,8], [3,4,9], [3,5,7], [3,5,9]
#    The falling path with the smallest sum is [1,5,7], so the answer is 13.
#
#    Example 2:
#
#    Input: grid = [[7]]
#    Output: 7
#
#
#
#    Constraints:
#
#        n == grid.length == grid[i].length
#        1 <= n <= 200
#        -99 <= grid[i][j] <= 99
#
#


import math


class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        dy = dx = len(grid)

        if dx == 1:
            return grid[dy-1][0]

        for idx_y in range(1, dy):
            line = grid[idx_y-1]

            min_val = min(line)
            second_min = None

            for idx_x in range(0,dx):
                if line[idx_x] == min_val:

                    if second_min is None:
                        v1 = min(line[0:idx_x]) if idx_x > 0 else math.inf
                        v2 = min(line[(idx_x+1):]) if idx_x < (dx-1) else math.inf 

                        val = second_min = min(v1, v2)
                    else:
                        val = second_min
                else:
                    val = min_val
                
                grid[idx_y][idx_x] += val

        #for idx_y in range(0, dy):
        #    print(grid[idx_y])

        return min(grid[dy-1])

        def slow(grid):
            dy = len(grid)
            dx = len(grid[0])

            if dx == 1:
                return grid[dy-1][0]

            for idx_y in range(1, dy):
                line = grid[idx_y-1]

                grid[idx_y][0] += min(line[1:])
                grid[idx_y][dx-1] += min(line[:-1])

                for idx_x in range(1,dx-1):                                    
                    grid[idx_y][idx_x] += min(min(line[0:idx_x]), min(line[(idx_x+1):]))

            #for idx_y in range(0, dy):
            #    print(grid[idx_y])

            return min(grid[dy-1])
                    
