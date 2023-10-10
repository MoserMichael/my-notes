# 52. N-Queens II
# Hard
#The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
#
#Given an integer n, return the number of distinct solutions to the n-queens puzzle.
#
#
#
#Example 1:
#
#Input: n = 4
#Output: 2
#Explanation: There are two distinct solutions to the 4-queens puzzle as shown.
#
#Example 2:
#
#Input: n = 1
#Output: 1
#
#
#
#Constraints:
#
#    1 <= n <= 9
#

class Solution:
    def totalNQueens(self, n: int) -> int:
        Solution.num_solutions = 0
        Solution.imp(n, 0, [])
        return Solution.num_solutions

    @staticmethod
    def imp(size_n, n_pos, stack):
        if n_pos == size_n:
            Solution.num_solutions += 1
            return

        for idx in range(0, size_n, 1):
            stack.append(idx)
            if Solution.conflict(stack):
                Solution.imp(size_n, n_pos+1, stack)
            stack.pop()

    @staticmethod
    def conflict(stack):
        pos_last = stack[-1]
        idx_last = len(stack) - 1

        for idx in range(0, len(stack)-1):
            pos = stack[idx]

            if abs(pos-pos_last) == abs(idx_last - idx) or pos_last == pos:
                return False

        return True
