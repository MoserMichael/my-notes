# 1380. Lucky Numbers in a Matrix
# Easy
#
#    Given an m x n matrix of distinct numbers, return all lucky numbers in the matrix in any order.
#
#    A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.
#
#
#
#    Example 1:
#
#    Input: matrix = [[3,7,8],[9,11,13],[15,16,17]]
#    Output: [15]
#    Explanation: 15 is the only lucky number since it is the minimum in its row and the maximum in its column.
#
#    Example 2:
#
#    Input: matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
#    Output: [12]
#    Explanation: 12 is the only lucky number since it is the minimum in its row and the maximum in its column.
#
#    Example 3:
#
#    Input: matrix = [[7,8],[1,2]]
#    Output: [7]
#    Explanation: 7 is the only lucky number since it is the minimum in its row and the maximum in its column.
#
#
#
#    Constraints:
#
#        m == mat.length
#        n == mat[i].length
#        1 <= n, m <= 50
#        1 <= matrix[i][j] <= 105.
#        All elements in the matrix are distinct.
#



class Entry:
    def __init__(self, val, pos_set):
        self.val = val
        self.pos_set = pos_set

class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:

        def find_col(x_pos):
            pos_set = set()
            max_val = -math.inf
            for y in range(dy):
                if matrix[y][x_pos] > max_val:
                    max_val = matrix[y][x_pos]
                    pos_set.clear()
                    pos_set.add(y)
                elif matrix[y][x_pos] == max_val:
                    pos_set.add(y)

            return Entry(max_val, pos_set)

        def find_row(y_pos):
            pos_set = set()
            min_val = math.inf
            for x in range(dx):
                if matrix[y_pos][x] < min_val:
                    min_val = matrix[y_pos][x]
                    pos_set.clear()
                    pos_set.add(x)
                elif matrix[y_pos][x] == min_val:
                    pos_set.add(x)

            return Entry(min_val, pos_set)


        dx = len(matrix[0])
        dy = len(matrix)

        rowEntry = []
        colEntry = []

        for x_idx in range(dx):
            colEntry.append( find_col(x_idx) )

        for y_idx in range(dy):
            rowEntry.append( find_row(y_idx) )

        ret = []

        for x_idx, entry in enumerate(rowEntry):
            for y_min in entry.pos_set:
                if x_idx in colEntry[y_min].pos_set:
                    ret.append( entry.val)

        return ret





