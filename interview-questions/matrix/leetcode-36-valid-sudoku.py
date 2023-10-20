# 36. Valid Sudoku
# Medium
#Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
#
#    Each row must contain the digits 1-9 without repetition.
#    Each column must contain the digits 1-9 without repetition.
#    Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
#
#Note:
#
#    A Sudoku board (partially filled) could be valid but is not necessarily solvable.
#    Only the filled cells need to be validated according to the mentioned rules.
#
# 
#
#Example 1:
#
#Input: board = 
#[["5","3",".",".","7",".",".",".","."]
#,["6",".",".","1","9","5",".",".","."]
#,[".","9","8",".",".",".",".","6","."]
#,["8",".",".",".","6",".",".",".","3"]
#,["4",".",".","8",".","3",".",".","1"]
#,["7",".",".",".","2",".",".",".","6"]
#,[".","6",".",".",".",".","2","8","."]
#,[".",".",".","4","1","9",".",".","5"]
#,[".",".",".",".","8",".",".","7","9"]]
#Output: true
#
#Example 2:
#
#Input: board = 
#[["8","3",".",".","7",".",".",".","."]
#,["6",".",".","1","9","5",".",".","."]
#,[".","9","8",".",".",".",".","6","."]
#,["8",".",".",".","6",".",".",".","3"]
#,["4",".",".","8",".","3",".",".","1"]
#,["7",".",".",".","2",".",".",".","6"]
#,[".","6",".",".",".",".","2","8","."]
#,[".",".",".","4","1","9",".",".","5"]
#,[".",".",".",".","8",".",".","7","9"]]
#Output: false
#Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
#
# 
#
#Constraints:
#
#    board.length == 9
#    board[i].length == 9
#    board[i][j] is a digit 1-9 or '.'.


#
#    # Intuition
#    The same check for repetitions, but multiple ways to iterate over the board (by row, by column, by square)
#
#    # Approach
#    Have one iterator function (function iter), pass the kind of iteration as argument (argument mode) the number of row/column/square is the second argument (argument num)
#
#    For each iteration: reset the same set object, check for repetition by adding to the set (supposedly O(1))
#
#    # Complexity
#    - Time complexity:
#    Passing over the same board nime times, each check for repetition is O(1). Therefore complexity is - $$O(m*n)$$ m - rows n - columns;
#
#    - Space complexity:
#    The set can have at most nine entries, so it's constant.
#
#    # Code
#
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        repeat_set = set()
        for mode in range(0, 3):
            for idx in range(0, 9):
                repeat_set = set()
                for y_pos, x_pos in Solution.iter(mode, idx):
                    num = board[y_pos][x_pos]
                    if num != ".":
                        if num in repeat_set:
                            return False
                        repeat_set.add(num)

        return True


    def iter(mode, num):
        if mode == 0:
            # row iterator
            for idx in range(0, 9):
                yield (num, idx)
        elif mode == 1:
            # columns
            for idx in range(0, 9):
                yield (idx, num)
        else:
            x_pos = (num // 3) * 3
            y_pos = (num * 3) % 9

            for y_idx in range(0, 3):
                for x_idx in range(0, 3):
                    yield (y_idx + y_pos, x_idx + x_pos)


