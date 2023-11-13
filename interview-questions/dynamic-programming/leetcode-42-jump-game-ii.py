# 45. Jump Game II
# Medium
#
#    You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].
#
#    Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:
#
#        0 <= j <= nums[i] and
#        i + j < n
#
#    Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].
#
#
#
#    Example 1:
#
#    Input: nums = [2,3,1,1,4]
#    Output: 2
#    Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
#
#    Example 2:
#
#    Input: nums = [2,3,0,1,4]
#    Output: 2
#
#
#
#    Constraints:
#
#        1 <= nums.length <= 104
#        0 <= nums[i] <= 1000
#        It's guaranteed that you can reach nums[n - 1].
#



import math

class Solution:
    def jump(self, nums: List[int]) -> int:
        #return Solution.withMemo(nums)
        return Solution.withTable(nums)

    def withTable(nums):

        if len(nums) == 0:
            return 0

        nums[len(nums)-1] = 0

        for xpos in range(len(nums)-2,-1,-1):
            min_steps = math.inf

            max_pos = min(len(nums)-1, xpos + nums[xpos])
            for dx in range(max_pos, xpos, -1):
                min_steps = min(min_steps, nums[dx])
            nums[xpos] = min_steps + 1

        return nums[0]



    def withMemo(nums):
        memo = {}
        ret = Solution.rec(nums, 0, memo)
        return ret


    def rec(nums, pos, memo):
        if pos >= len(nums):
            return math.inf
        if pos == len(nums)-1:
            return 0

        if pos in memo:
            return memo[pos]

        min_steps = math.inf
        for step in range(nums[pos],0,-1):
            res = Solution.rec(nums, pos + step, memo)
            min_steps = min(min_steps, res)

        min_steps += 1

        memo[pos] = min_steps

        return min_steps



