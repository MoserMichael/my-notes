# 9. Word Search
# Medium
#Given an m x n grid of characters board and a string word, return true if word exists in the grid.
#
#The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.
#
#
#
#Example 1:
#
#Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
#Output: true
#
#Example 2:
#
#Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
#Output: true
#
#Example 3:
#
#Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
#Output: false
#
#
#
#Constraints:
#
#    m == board.length
#    n = board[i].length
#    1 <= m, n <= 6
#    1 <= word.length <= 15
#    board and word consists of only lowercase and uppercase English letters.
#
#
#
#Follow up: Could you use search pruning to make your solution faster with a larger board?
#


class Solution:
    moves = [ (-1,0), (1,0), (0, -1), (0, 1) ]

    def exist(self, board: List[List[str]], word: str) -> bool:
        return Solution.walkBoard( word, board)

    @staticmethod
    def walkBoard( word, board):

        visitedSet = set()

        for pos_x in range(0, len(board[0])):
            for pos_y in range(0, len(board)):
                if Solution.walkWordRec( pos_x, pos_y, word, 0, board, visitedSet):
                    return True
        return False

    @staticmethod
    def walkWordRec(pos_x, pos_y, word, word_pos, board, visitedSet):

        if board[pos_y][pos_x] != word[word_pos]:
            return False

        word_pos += 1
        if word_pos == len(word):
            return True

        key = ( pos_x, pos_y )
        visitedSet.add(key)

        ret = False
        for pos in Solution.adjacentLetters(pos_x, pos_y, board, visitedSet, word[word_pos]):

            ret = Solution.walkWordRec( pos[0], pos[1], word, word_pos, board, visitedSet)
            if ret:
                break

        visitedSet.remove(key)

        return ret

    @staticmethod
    def adjacentLetters(pos_x, pos_y, board, visitedSet, expectedLetter):
        retPos = []

        for move in Solution.moves:
            p_x = pos_x + move[0]
            p_y = pos_y + move[1]

            if 0 <= p_x < len(board[0]) and 0 <= p_y < len(board):
                if expectedLetter == board[p_y][p_x]:
                    key = (p_x, p_y)
                    if key not in visitedSet:
                        retPos.append( key )

        return retPos


