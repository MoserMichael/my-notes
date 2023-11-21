# 498. Diagonal Traverse
# Medium
#
#    Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.
#
#
#
#    Example 1:
#
#    Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
#    Output: [1,2,4,7,5,3,6,8,9]
#
#    Example 2:
#
#    Input: mat = [[1,2],[3,4]]
#    Output: [1,2,3,4]
#
#
#
#    Constraints:
#
#        m == mat.length
#        n == mat[i].length
#        1 <= m, n <= 104
#        1 <= m * n <= 104
#        -105 <= mat[i][j] <= 105
#



class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        #return Solution.slowAndSimple(mat)
        return Solution.aBitFaster(mat)


    def aBitFaster(mat):
        rows = len(mat[0])
        cols = len(mat)
        expected_len = rows * cols
        row_len = 1

        x = y = 0
        dx=1
        dy=-1
        idx = 0

        ret = []

        while idx < expected_len:

            ret.append(mat[y][x])

            x+=dx
            y+=dy
            idx += 1

            if x >= rows:
                x -= 1
                y += 2
                dx = -dx
                dy = -dy
            elif y >= cols:
                y -= 1
                x += 2
                dx = -dx
                dy = -dy
            elif x < 0:
                x += 1
                dx = -dx
                dy = -dy
            elif y < 0:
                y += 1
                dx = -dx
                dy = -dy

        return ret





    def slowAndSimple(mat):
        rows = len(mat[0])
        cols = len(mat)
        reverse =  True
        ret = []

        for idx in range(0, rows+cols):

            x = idx
            y = 0

            line = []

            for dist in range(0, cols):
                if 0 <= x < rows and 0 <= y < cols:
                    line.append(mat[y][x])
                x -= 1
                y += 1

            if reverse:
                line.reverse()
            reverse = not reverse

            ret.extend(line)

        return ret




