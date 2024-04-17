# 85. Maximal Rectangle
# Hard
#
#    Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.
#
#
#
#    Example 1:
#
#    Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
#    Output: 6
#    Explanation: The maximal rectangle is shown in the above picture.
#
#    Example 2:
#
#    Input: matrix = [["0"]]
#    Output: 0
#
#    Example 3:
#
#    Input: matrix = [["1"]]
#    Output: 1
#
#
#
#    Constraints:
#
#        rows == matrix.length
#        cols == matrix[i].length
#        1 <= row, cols <= 200
#        matrix[i][j] is '0' or '1'.
#


# don't do it like this. This solution sux!

class Solution:

    def add_rect(self, x, y):
        self.max_size = max(self.max_size, x * y)

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        self.max_size = 0

        x_size = len(matrix[0])
        y_size = len(matrix)

        tmp_row = [None] * x_size
        tmp = [tmp_row.copy() for _ in range(y_size)]

        for y in range(y_size):
            x = 0
            while x < x_size:
                run_len = 0
                while (x + run_len) < x_size and matrix[y][x + run_len] == "1":
                    run_len += 1

                    # run of ones.
                    if y > 0 and tmp[y-1][x+run_len-1]:
                        res_rect = []

                        has_run_len = False
                        for r in tmp[y-1][x+run_len-1]:
                            min_w = min(r[0], run_len)
                            res_rect.append( (min_w, r[1]+1) )
                            self.add_rect(min_w, r[1]+1)
                            if min_w == run_len:
                                has_run_len = True
                        if not has_run_len:
                            res_rect.append( (run_len, 1) )
                            self.add_rect( run_len, 1 )
                        tmp[y][x+run_len-1] = res_rect
                    else:
                        tmp[y][x+run_len-1] = [ (run_len, 1)]
                        self.add_rect(run_len, 1)


                x += run_len + 1

        return self.max_size
