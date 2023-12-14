# 1582. Special Positions in a Binary Matrix
# Easy
#
#    Given an m x n binary matrix mat, return the number of special positions in mat.
#
#    A position (i, j) is called special if mat[i][j] == 1 and all other elements in row i and column j are 0 (rows and columns are 0-indexed).
#
#
#
#    Example 1:
#
#    Input: mat = [[1,0,0],[0,0,1],[1,0,0]]
#    Output: 1
#    Explanation: (1, 2) is a special position because mat[1][2] == 1 and all other elements in row 1 and column 2 are 0.
#
#    Example 2:
#
#    Input: mat = [[1,0,0],[0,1,0],[0,0,1]]
#    Output: 3
#    Explanation: (0, 0), (1, 1) and (2, 2) are special positions.
#
#
#
#    Constraints:
#
#        m == mat.length
#        n == mat[i].length
#        1 <= m, n <= 100
#        mat[i][j] is either 0 or 1.
#
#



class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:

        self.x_sum = {}

        dx = len(mat[0])
        dy = len(mat)

        ret = 0

        for y_idx in range(0, dy):

            row_s =  sum(mat[y_idx])

            if row_s != 1:
                continue

            for x_idx in range(0, dx):
                if mat[y_idx][x_idx] == 1:
                    col_s = self.make_col_sum(mat, x_idx)
                    if col_s == 1:
                        ret += 1
                        # only one per row possible.
                        break

        return ret

    def make_col_sum(self, mat, col_idx):

        if col_idx in self.x_sum:
            return self.x_sum[col_idx]

        res = 0

        for idx in range(0, len(mat)):
            res += mat[idx][col_idx]

        self.x_sum[col_idx] = res

        return res
