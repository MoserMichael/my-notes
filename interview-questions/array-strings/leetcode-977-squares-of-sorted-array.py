# 977. Squares of a Sorted Array
# Easy
#    Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
#
#
#
#    Example 1:
#
#    Input: nums = [-4,-1,0,3,10]
#    Output: [0,1,9,16,100]
#    Explanation: After squaring, the array becomes [16,1,0,9,100].
#    After sorting, it becomes [0,1,9,16,100].
#
#    Example 2:
#
#    Input: nums = [-7,-3,2,3,11]
#    Output: [4,9,9,49,121]
#
#
#
#    Constraints:
#
#        1 <= nums.length <= 104
#        -104 <= nums[i] <= 104
#        nums is sorted in non-decreasing order.
#
#
#    Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?
#


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        pos_squares = []
        neg_squares = []
        for n in nums:
            if n < 0:
                neg_squares.insert(0, n ** 2)
            else:
                pos_squares.append(n ** 2)

        pos_idx = neg_idx = 0

        res = []
        while pos_idx < len(pos_squares) and neg_idx < len(neg_squares):
            if pos_squares[pos_idx] < neg_squares[neg_idx]:
                res.append(pos_squares[pos_idx])
                pos_idx += 1
            else:
                res.append(neg_squares[neg_idx])
                neg_idx += 1

        res += pos_squares[pos_idx:len(pos_squares)]
        res += neg_squares[neg_idx:len(neg_squares)]

        return res

