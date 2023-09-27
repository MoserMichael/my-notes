# 2352. Equal Row and Column Pairs
# Medium
#Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.
#
#A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).
#
# 
#
#Example 1:
#
#Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
#Output: 1
#Explanation: There is 1 equal row and column pair:
#- (Row 2, Column 1): [2,7,7]
#
#Example 2:
#
#Input: grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
#Output: 3
#Explanation: There are 3 equal row and column pairs:
#- (Row 0, Column 0): [3,1,2,2]
#- (Row 2, Column 2): [2,4,2,2]
#- (Row 3, Column 2): [2,4,2,2]
#
# 
#
#Constraints:
#
#    n == grid.length == grid[i].length
#    1 <= n <= 200
#    1 <= grid[i][j] <= 105
#


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:

        rowMap = {}
        repeatedColumns = 0

        for row in grid:
            key=tuple(row)
            if key in rowMap:
                rowMap[key] += 1
            else:
                rowMap[key] = 1

        for i in range(0,len(grid[0])):
            column = []
            for j in range(0,len(grid)):
                column.append(grid[j][i])

            key = tuple(column)
            if key in rowMap:
                repeatedColumns += rowMap[key]


        return repeatedColumns

