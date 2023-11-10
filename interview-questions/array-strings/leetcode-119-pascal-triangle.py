# 119. Pascal's Triangle II
# Easy
#
#    Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
#
#    In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
#
#     
#
#    Example 1:
#
#    Input: rowIndex = 3
#    Output: [1,3,3,1]
#
#    Example 2:
#
#    Input: rowIndex = 0
#    Output: [1]
#
#    Example 3:
#
#    Input: rowIndex = 1
#    Output: [1,1]
#
#     
#
#    Constraints:
#
#        0 <= rowIndex <= 33
#
#     
#
#    Follow up: Could you optimize your algorithm to use only O(rowIndex) extra space?
#

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex < 2:
            return [1] * (rowIndex + 1)

        row = [1] * (rowIndex+1)

        for level in range(2, rowIndex+1):
            prev_idx = row[0]
            for idx in range(1, level):
                next_prev_idx = row[idx]
                row[idx] = row[idx] + prev_idx
                prev_idx = next_prev_idx

        return row

