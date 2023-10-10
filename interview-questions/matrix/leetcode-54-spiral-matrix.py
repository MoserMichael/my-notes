# 54. Spiral Matrix
# Medium
#Given an m x n matrix, return all elements of the matrix in spiral order.
#
# 
#
#Example 1:
#
#Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
#Output: [1,2,3,6,9,8,7,4,5]
#
#Example 2:
#
#Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
#Output: [1,2,3,4,8,12,11,10,9,5,6,7]
#
# 
#
#Constraints:
#
#    m == matrix.length
#    n == matrix[i].length
#    1 <= m, n <= 10
#    -100 <= matrix[i][j] <= 100
#


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        size_x = len(matrix[0])
        size_y = len(matrix)

        row_matrix = [0] * size_x
        visit_matrix = []
        for idx in range(0, size_y):
            visit_matrix.append( row_matrix.copy() )

        pos_x = pos_y = 0
        ret = [ matrix[0][0] ]

        visited = 1
        visit_matrix[pos_y][pos_x] = 1

        while True:

            pos_x += 1
            while pos_x < size_x:
                if visit_matrix[pos_y][pos_x]:
                    break
                visit_matrix[pos_y][pos_x] = 1
                ret.append( matrix[pos_y][pos_x] )
                pos_x += 1
                visited += 1
            pos_x -= 1

            if visited >= size_x * size_y:
                break

            pos_y += 1
            while pos_y < size_y:
                if visit_matrix[pos_y][pos_x]:
                    break
                visit_matrix[pos_y][pos_x] = 1
                ret.append( matrix[pos_y][pos_x] )
                pos_y += 1
                visited += 1
            pos_y -= 1

            if visited >= size_x * size_y:
                break

            pos_x -= 1
            while pos_x >= 0:
                if visit_matrix[pos_y][pos_x]:
                    break
                visit_matrix[pos_y][pos_x] = 1
                ret.append( matrix[pos_y][pos_x] )
                pos_x -= 1
                visited += 1
            pos_x += 1

            if visited >= size_x * size_y:
                break

            pos_y -= 1
            while pos_y >= 0:
                if visit_matrix[pos_y][pos_x]:
                    break
                visit_matrix[pos_y][pos_x] = 1
                ret.append( matrix[pos_y][pos_x] )
                pos_y -= 1
                visited += 1
            pos_y += 1

            if visited >= size_x * size_y:
                break

        return ret


