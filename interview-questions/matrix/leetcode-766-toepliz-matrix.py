# 766. Toeplitz Matrix
# Easy
#
#    Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.
#
#    A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.
#
#     
#
#    Example 1:
#
#    Input: matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
#    Output: true
#    Explanation:
#    In the above grid, the diagonals are:
#    "[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
#    In each diagonal all elements are the same, so the answer is True.
#
#    Example 2:
#
#    Input: matrix = [[1,2],[2,2]]
#    Output: false
#    Explanation:
#    The diagonal "[1, 2]" has different elements.
#
#     
#
#    Constraints:
#
#        m == matrix.length
#        n == matrix[i].length
#        1 <= m, n <= 20
#        0 <= matrix[i][j] <= 99
#
#     
#
#    Follow up:
#
#        What if the matrix is stored on disk, and the memory is limited such that you can only load at most one row of the matrix into the memory at once?
#        What if the matrix is so large that you can only load up a partial row into the memory at once?
#
#


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        return Solution.one_pass_check(matrix)
        #return Solution.multiple_pass_easy(matrix)

    def one_pass_check(matrix):
        dx = len(matrix[0])
        dy = len(matrix)

        for y in range(1, dy):
            for x in range(y,dx):
                if matrix[y][x] != matrix[y-1][x-1]:
                    return False

            for x in range(1, min(dx,y) ):
                if matrix[y][x] != matrix[y-1][x-1]:
                    return False

        return True

    def multiple_pass_easy(matrix):
        dx = len(matrix[0])
        dy = len(matrix)

        def check_diag(x,y):
            move = 1
            first = matrix[y][x]
            while True:
                if x + move >= dx or y + move >= dy:
                    break
                if matrix[y+move][x+move] != first:
                    return False
                move += 1
            return True

        for pos in range(dx-1):
            if not check_diag(pos, 0):
                return False

        for pos in range(1, dy-1):
            if not check_diag(0, pos):
                return False

        return True

