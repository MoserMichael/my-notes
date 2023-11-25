# 222. Queens That Can Attack the King
# Medium
#
#    On a 0-indexed 8 x 8 chessboard, there can be multiple black queens ad one white king.
#
#    You are given a 2D integer array queens where queens[i] = [xQueeni, yQueeni] represents the position of the ith black queen on the chessboard. You are also given an integer array king of length 2 where king = [xKing, yKing] represents the position of the white king.
#
#    Return the coordinates of the black queens that can directly attack the king. You may return the answer in any order.
#
#
#
#    Example 1:
#
#    Input: queens = [[0,1],[1,0],[4,0],[0,4],[3,3],[2,4]], king = [0,0]
#    Output: [[0,1],[1,0],[3,3]]
#    Explanation: The diagram above shows the three queens that can directly attack the king and the three queens that cannot attack the king (i.e., marked with red dashes).
#
#    Example 2:
#
#    Input: queens = [[0,0],[1,1],[2,2],[3,4],[3,5],[4,4],[4,5]], king = [3,3]
#    Output: [[2,2],[3,4],[4,4]]
#    Explanation: The diagram above shows the three queens that can directly attack the king and the three queens that cannot attack the king (i.e., marked with red dashes).
#
#
#
#    Constraints:
#
#        1 <= queens.length < 64
#        queens[i].length == king.length == 2
#        0 <= xQueeni, yQueeni, xKing, yKing < 8
#        All the given positions are unique.
#
#

class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], k: List[int]) -> List[List[int]]:

        board = Solution.initBoard(queens)
        ret = []

        for q in queens:
            if q[0] == k[0]:
                dir_x = 0
                dir_y = 1 if q[1]<k[1] else -1
            elif q[1] == k[1]:
                dir_y = 0
                dir_x = 1 if q[0]<k[0] else -1
            elif abs(q[0]-k[0]) == abs(q[1] - k[1]):
                dir_x = 1 if q[0]<k[0] else -1
                dir_y = 1 if q[1]<k[1] else -1
            else:
                continue


            q_x = q[0]
            q_y = q[1]

            can_eat = True
            while True:
                q_x += dir_x
                q_y += dir_y

                if q_x in board and q_y in board[q_x]:
                    can_eat = False
                    break

                if q_x == k[0] and q_y == k[1]:
                    break

            if can_eat:
                ret.append(q)

        return ret


    def initBoard(queens):
        board = {}

        for q in queens:
            mp = board.setdefault(q[0],{})
            mp[q[1]] = 1

        return board





