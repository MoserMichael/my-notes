# 51. N-Queens
# Hard
#The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
#
#Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.
#
#Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.
#
# 
#
#Example 1:
#
#Input: n = 4
#Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
#Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
#
#Example 2:
#
#Input: n = 1
#Output: [["Q"]]
#
# 
#
#Constraints:
#
#    1 <= n <= 9
#



class Solution:

    def solveNQueens(self, n: int) -> int:
        ret = []
        Solution.imp(n, 0, [], ret)
        return ret

    @staticmethod
    def imp(size_n, n_pos, stack, ret):
        if n_pos == size_n:
            Solution.encode(ret, stack, size_n)
            return

        if n_pos == 0:

            # use symmetry along the x axis.
            m_size = half = size_n // 2

            if size_n % 2 == 1:
                m_size += 1

            for idx in range(0, m_size, 1):
                stack.append(idx)
                if Solution.conflict(stack):
                    res = Solution.imp(size_n, n_pos+1, stack, ret)
                stack.pop()

        else:
            for idx in range(0, size_n, 1):
                stack.append(idx)
                if Solution.conflict(stack):
                    Solution.imp(size_n, n_pos+1, stack, ret)
                stack.pop()


    @staticmethod
    def encode(rval, stack, size_n):

        #print(stack)

        ret = []
        for s in stack:
            s = ('.' * s) + 'Q' + ('.' * (size_n-1-s))
            ret.append(s)
        rval.append(ret)

        if stack[0] < size_n // 2:
            ret = []
            for s in stack:
                s = size_n-1 - s
                s = ('.' * s) + 'Q' + ('.' * (size_n-1-s))
                ret.append(s)
            rval.append(ret)


    @staticmethod
    def conflict(stack):
        pos_last = stack[-1]
        idx_last = len(stack) - 1

        for idx in range(0, len(stack)-1):
            pos = stack[idx]
            if abs(pos-pos_last) == abs(idx_last - idx) or pos_last == pos:
                return False

        return True
