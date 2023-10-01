# 209. Minimum Size Subarray Sum
# Medium
#Given an array of positive integers nums and a positive integer target, return the minimal length of a
#subarray
#whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.
#
# 
#
#Example 1:
#
#Input: target = 7, nums = [2,3,1,2,4,3]
#Output: 2
#Explanation: The subarray [4,3] has the minimal length under the problem constraint.
#
#Example 2:
#
#Input: target = 4, nums = [1,4,4]
#Output: 1
#
#Example 3:
#
#Input: target = 11, nums = [1,1,1,1,1,1,1,1]
#Output: 0
#
# 
#
#Constraints:
#
#    1 <= target <= 109
#    1 <= nums.length <= 105
#    1 <= nums[i] <= 104
#
# 
#Follow up: If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log(n)).
#

import math

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        if not len(nums):
            return 0

        left = 0
        right = 0
        sum = nums[0]
        max_len = math.inf

        while left < len(nums):

            #print(f"left {left} right {right} sum {sum} max_len: {max_len} cur_len: {right-left+1}")
            if sum >= target:
                if max_len > (right-left+1):
                    max_len = right-left+1
                    if max_len == 1:
                        break

            if sum <= target and right < len(nums):
                right += 1
                if right < len(nums):
                    sum += nums[right]
            else:
                sum -= nums[left]
                left += 1

        if max_len == math.inf:
            return 0
        return max_len

