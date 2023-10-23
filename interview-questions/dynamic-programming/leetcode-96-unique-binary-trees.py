# 96. Unique Binary Search Trees
# Medium
#    Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.
#
#
#
#    Example 1:
#
#    Input: n = 3
#    Output: 5
#
#    Example 2:
#
#    Input: n = 1
#    Output: 1
#
#
#
#    Constraints:
#
#        1 <= n <= 19
#

class Solution:
    def numTrees(self, n: int) -> int:
        arr = [0] * (n+1)

        arr[1] = 1

        for idx in range(2, len(arr)):
            sm = 0

            for size_left in range(0,idx):
                size_right = idx - 1 - size_left
                if arr[size_left] != 0 and arr[size_right] != 0:
                    add_size = arr[size_left] * arr[size_right]
                else:
                    add_size =  max(arr[size_left], arr[size_right])
                sm += add_size

            arr[idx] = sm
            print(f"res: {sm} arr: - {arr}")

        return arr[-1]

