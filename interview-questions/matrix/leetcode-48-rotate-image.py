# 48. Rotate Image
# Medium
#You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
#
#You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
#
#
#
#Example 1:
#
#Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
#Output: [[7,4,1],[8,5,2],[9,6,3]]
#
#Example 2:
#
#Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
#Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
#
#
#
#Constraints:
#
#    n == matrix.length == matrix[i].length
#    1 <= n <= 20
#    -1000 <= matrix[i][j] <= 1000
#
#


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        square_size = len(matrix)
        assert len(matrix[0]) == square_size

        pos_x = pos_y = 0

        for offset in range(0, int(square_size/2)):
            Solution.rotateOneRow(matrix, pos_x, pos_y, square_size)

            pos_x += 1
            pos_y += 1
            square_size -= 2

    @staticmethod
    def rotateOneRow(matrix, pos_x, pos_y, square_size):
        if square_size < 2:
            return
        for offset in range(0, square_size-1):
            Solution.rotateOneTurn(matrix, pos_x, pos_y, square_size, offset)


    @staticmethod
    def rotateOneTurn(matrix, pos_x, pos_y, square_size,  offset):
        last_val = matrix[pos_y][pos_x + offset]

        swaps = [

            #(pos_x + offset, pos_y) =>
             (pos_x + square_size -1, pos_y + offset),

             #(pos_x + square_size -1, pos_y + offset) =>
             (pos_x + square_size - 1 - offset, pos_y + square_size - 1),

             #(pos_x + square_size - 1 - offset, posy + square_size - 1) =>
             (pos_x, pos_y + square_size - 1 - offset),

             #(pos_x, pos_y + square_size - 1 - offset) =>
             (pos_x + offset, pos_y)
        ]

        for swap in swaps:
             next_last_val = matrix[swap[1]][swap[0]]
             matrix[swap[1]][swap[0]] = last_val
             last_val = next_last_val


