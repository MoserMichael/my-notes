# 73. Set Matrix Zeroes
# Medium
#Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
#
#You must do it in place.
#
# 
#
#Example 1:
#
#Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
#Output: [[1,0,1],[0,0,0],[1,0,1]]
#
#Example 2:
#
#Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
#Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
#
# 
#
#Constraints:
#
#    m == matrix.length
#    n == matrix[0].length
#    1 <= m, n <= 200
#    -231 <= matrix[i][j] <= 231 - 1
#
# 
#
#Follow up:
#
#    A straightforward solution using O(mn) space is probably a bad idea.
#    A simple improvement uses O(m + n) space, but still not the best solution.
#    Could you devise a constant space solution?


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        #Solution.withSet(matrix)
        Solution.withConstantSpace(matrix)

    def withConstantSpace(matrix):
        x_zero_set = False
        y_zero_set = False

        # shift
        for y_idx in range(1, len(matrix)):
            matrix[y_idx][0] <<=  1

        for x_idx in range(1, len(matrix[0])):
            matrix[0][x_idx] <<=  1

        # detect
        for y_idx in range(0, len(matrix)):
            for x_idx in range(0, len(matrix[0])):
                if matrix[y_idx][x_idx] == 0:
                    if y_idx != 0:
                        matrix[y_idx][0] = matrix[y_idx][0] | 1
                    else:
                        x_zero_set = True

                    if x_idx != 0:
                        matrix[0][x_idx] = matrix[0][x_idx] | 1
                    else:
                        y_zero_set = True


        # remove except first row column
        for x_idx in range(1, len(matrix[0])):
            if matrix[0][x_idx] & 1 != 0:
                Solution.reset_col(x_idx, matrix, 1)

        for y_idx in range(1, len(matrix)):
            if matrix[y_idx][0] & 1 != 0:
                Solution.reset_row(y_idx, matrix, 1)

        # deal with first row column
        for y_idx in range(1, len(matrix)):
            if  matrix[y_idx][0] & 1 != 0:
                matrix[y_idx][0] = 0
            else:
                matrix[y_idx][0] >>= 1

        for x_idx in range(1, len(matrix[0])):
            if matrix[0][x_idx] & 1 != 0:
                matrix[0][x_idx] = 0
            else:
                matrix[0][x_idx]  >>= 1

        if x_zero_set:
            Solution.reset_row(0, matrix)

        if y_zero_set:
            Solution.reset_col(0, matrix)

    def withSet(matrix):
        row_set = set()
        col_set = set()

        for y_idx in range(0, len(matrix)):
            for x_idx in range(0, len(matrix[0])):
                if matrix[y_idx][x_idx] == 0:
                    row_set.add(y_idx)
                    col_set.add(x_idx)

        for r in row_set:
            Solution.reset_row(r, matrix)

        for r in col_set:
            Solution.reset_col(r, matrix)

    def reset_row(y_idx, matrix, offset = 0):
        for x_idx in range(offset, len(matrix[0])):
            matrix[y_idx][x_idx] = 0

    def reset_col(x_idx, matrix, offset = 0):
        for y_idx in range(offset, len(matrix)):
            matrix[y_idx][x_idx] = 0





