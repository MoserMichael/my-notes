# 130. Surrounded Regions
# Medium
#
#    Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.
#
#    A region is captured by flipping all 'O's into 'X's in that surrounded region.
#
#
#
#    Example 1:
#
#    Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
#    Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
#    Explanation: Notice that an 'O' should not be flipped if:
#    - It is on the border, or
#    - It is adjacent to an 'O' that should not be flipped.
#    The bottom 'O' is on the border, so it is not flipped.
#    The other three 'O' form a surrounded region, so they are flipped.
#
#    Example 2:
#
#    Input: board = [["X"]]
#    Output: [["X"]]
#
#
#
#    Constraints:
#
#        m == board.length
#        n == board[i].length
#        1 <= m, n <= 200
#        board[i][j] is 'X' or 'O'.
#


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.board  = board
        self.x_size = len(board[0])
        self.y_size = len(board)
        self.all_visit = set()

        for x in range(1, self.x_size-1):
            for y in range(1, self.y_size-1):
                if board[y][x] != 'X' and (x, y) not in self.all_visit:
                    pos_set = set()

                    # find the location of zeros of an island
                    if self.recVisit(x, y, pos_set):
                        # if proper island - flip them
                        self.flipThem(pos_set)


    def flipThem(self, pos_set):
        for pos in pos_set:
            self.board[pos[1]][pos[0]] = 'X'


    # recursively visit all zeros, fill location of zeros, return True if proper island
    def recVisit(self, x, y, pos_set):

        p = (x,y)
        if p in pos_set: #self.all_visit:
            return True

        if x < 0 or x >= (self.x_size) or y < 0 or y >= self.y_size:
            return False

        if self.board[y][x] == "O":
            pos_set.add( (x,y) )
            self.all_visit.add( (x, y) )
            if not self.recVisit(x - 1, y, pos_set) or not self.recVisit(x + 1, y, pos_set) or not self.recVisit(x, y - 1, pos_set) or not self.recVisit(x, y + 1, pos_set):
                return False

        return True


