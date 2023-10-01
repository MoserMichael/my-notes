# 289. Game of Life
# Medium
#According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."
#
#The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):
#
#    Any live cell with fewer than two live neighbors dies as if caused by under-population.
#    Any live cell with two or three live neighbors lives on to the next generation.
#    Any live cell with more than three live neighbors dies, as if by over-population.
#    Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
#
#The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.
#
# 
#
#Example 1:
#
#Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
#Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
#
#Example 2:
#
#Input: board = [[1,1],[1,0]]
#Output: [[1,1],[1,1]]
#
# 
#
#Constraints:
#
#    m == board.length
#    n == board[i].length
#    1 <= m, n <= 25
#    board[i][j] is 0 or 1.
#
# 
#
#Follow up:
#
#    Could you solve it in-place? Remember that the board needs to be updated simultaneously: You cannot update some cells first and then use their updated values to update other cells.
#    In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches upon the border of the array (i.e., live cells reach the border). How would you address these problems?
#
#

class Solution:

    dpos = [
        (-1,-1), (0, -1), (1, -1),
        (-1, 0),          (1, 0),
        (-1, 1), (0, 1),  (1, 1)
    ]
    
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        changed_cells = []
        for idx_x in range(0, len(board[0])):
            for idx_y in range(0, len(board)):
                state = board[idx_y][idx_x]
                count = Solution.countAdjacent(idx_x, idx_y, board)
                new_state = -1
                if state == 1 and count < 2:
                    new_state = 0
                #elif state and (count == 2 or count == 3):
                #    pass
                elif state == 1 and (count > 3):
                    new_state = 0
                elif state == 0 and count == 3:
                    new_state = 1

                if new_state != -1:
                    #print(f"{idx_x}:{idx_y} => old_state: {state} count {count} / new_state {new_state}")
                    changed_cells.append( (idx_x, idx_y, new_state))

        #print(f"changed_cells {changed_cells}")
        for ch in changed_cells:
            board[ch[1]][ch[0]] = ch[2]

        


    @staticmethod
    def countAdjacent(pos_x, pos_y, board):
        count = 0
        for dp in Solution.dpos:
            x = pos_x + dp[0]
            y = pos_y + dp[1]
            if 0 <= x < len(board[0]) and 0 <= y < len(board):
                if board[y][x] == 1:
                    count += 1
        return count


