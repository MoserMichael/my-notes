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
        return Solution.imp(n, 0, [])

    @staticmethod
    def imp(size_n, n_pos, stack):
        if n_pos == size_n:
            return 1

        sum = 0

        if n_pos == 0:

            # use symmetry along the x axis.
            m_size = half = size_n // 2

            if size_n % 2 == 1:
                m_size += 1

            for idx in range(0, m_size, 1):
                stack.append(idx)
                if Solution.conflict(stack):
                    res = Solution.imp(size_n, n_pos+1, stack)
                    if idx < half:
                        res *= 2
                    sum += res
                stack.pop()

        else:
            for idx in range(0, size_n, 1):
                stack.append(idx)
                if Solution.conflict(stack):
                    sum += Solution.imp(size_n, n_pos+1, stack)
                stack.pop()

        return sum

    @staticmethod
    def conflict(stack):
        pos_last = stack[-1]
        idx_last = len(stack) - 1

        for idx in range(0, len(stack)-1):
            pos = stack[idx]
            if abs(pos-pos_last) == abs(idx_last - idx) or pos_last == pos:
                return False

        return True


