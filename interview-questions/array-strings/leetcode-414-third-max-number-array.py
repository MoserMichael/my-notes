# 414. Third Maximum Number
# Easy
#
#    Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.
#
#
#
#    Example 1:
#
#    Input: nums = [3,2,1]
#    Output: 1
#    Explanation:
#    The first distinct maximum is 3.
#    The second distinct maximum is 2.
#    The third distinct maximum is 1.
#
#    Example 2:
#
#    Input: nums = [1,2]
#    Output: 2
#    Explanation:
#    The first distinct maximum is 2.
#    The second distinct maximum is 1.
#    The third distinct maximum does not exist, so the maximum (2) is returned instead.
#
#    Example 3:
#
#    Input: nums = [2,2,3,1]
#    Output: 1
#    Explanation:
#    The first distinct maximum is 3.
#    The second distinct maximum is 2 (both 2's are counted together since they have the same value).
#    The third distinct maximum is 1.
#
#
#
#    Constraints:
#
#        1 <= nums.length <= 104
#        -231 <= nums[i] <= 231 - 1
#
#
#    Follow up: Can you find an O(n) solution?
#



import math

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        return Solution.thirdMaxNoRemove(nums)
        #return Solution.thirdMaxWithRemove(nums)

    # that's more like O(n) - but runs slower, doesn't use any library functions :-)
    def thirdMaxNoRemove(nums):
        if len(nums) != 0:
            m1 = max(nums)
        else:
            return math.inf

        if len(nums) == 0:
            return m1

        m2 = Solution.maxIgnoreLargerThan(nums, m1)
        if m2 == -math.inf:
            return m1

        m2 = Solution.maxIgnoreLargerThan(nums, m2)
        if m2 == -math.inf:
            return m1

        return m2


   # that's O(n) - but has lots of passes. (and runs slower than sort, because input array is probably relatively small :-)
    def maxIgnoreLargerThan(nums, thresh):
        maxNum = -math.inf
        for n in nums:
            if n < thresh and n > maxNum:
                maxNum = n
        return maxNum


    def thirdMaxWithRemove(nums):
        if len(nums) != 0:
            m1 = max(nums)
            nums = list(filter(lambda a: a != m1, nums))
        else:
            return math.inf

        if len(nums) != 0:
            m2 = max(nums)
            nums = list(filter(lambda a: a != m2, nums))
        else:
            return m1

        if len(nums) != 0:
            return max(nums)
        return m1


