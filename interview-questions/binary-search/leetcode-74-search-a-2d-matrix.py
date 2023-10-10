# 74. Search a 2D Matrix
# Medium
#You are given an m x n integer matrix matrix with the following two properties:
#
#    Each row is sorted in non-decreasing order.
#    The first integer of each row is greater than the last integer of the previous row.
#
#Given an integer target, return true if target is in matrix or false otherwise.
#
#You must write a solution in O(log(m * n)) time complexity.
#
#
#
#Example 1:
#
#Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
#Output: true
#
#Example 2:
#
#Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
#Output: false
#
#
#
#Constraints:
#
#    m == matrix.length
#    n == matrix[i].length
#    1 <= m, n <= 100
#    -104 <= matrix[i][j], target <= 104
#

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        matrix_dy = len(matrix)
        matrix_dx = len(matrix[0])

        return Solution.binSearch(target, 0, (matrix_dy * matrix_dx) - 1, matrix)


    def binSearch(target, low, high, matrix):
        #print(f"{low}..{high}")
        if low > high:
            return False
        mid = (low+high)//2

        num = Solution.get_n(mid, matrix)

        #print(f"[{mid}] == {num}")

        if num == target:
            return True
        elif num > target:
            return Solution.binSearch(target, 0, mid-1, matrix)
        return Solution.binSearch(target, mid+1, high, matrix)



    def get_n( idx, matrix):

        matrix_dy = len(matrix)
        matrix_dx = len(matrix[0])

        y = idx // matrix_dx
        x = idx % matrix_dx

        return matrix[y][x]

