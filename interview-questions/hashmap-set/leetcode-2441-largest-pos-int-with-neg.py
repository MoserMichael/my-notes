# 2441. Largest Positive Integer That Exists With Its Negative
# Easy
#
#    Given an integer array nums that does not contain any zeros, find the largest positive integer k such that -k also exists in the array.
#
#    Return the positive integer k. If there is no such integer, return -1.
#
#
#
#    Example 1:
#
#    Input: nums = [-1,2,-3,3]
#    Output: 3
#    Explanation: 3 is the only valid k we can find in the array.
#
#    Example 2:
#
#    Input: nums = [-1,10,6,7,-7,1]
#    Output: 7
#    Explanation: Both 1 and 7 have their corresponding negative values in the array. 7 has a larger value.
#
#    Example 3:
#
#    Input: nums = [-10,8,6,7,-2,-3]
#    Output: -1
#    Explanation: There is no a single valid k, we return -1.
#
#
#
#    Constraints:
#
#        1 <= nums.length <= 1000
#        -1000 <= nums[i] <= 1000
#        nums[i] != 0
#

class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        #return Solution.withSort(nums)
        return Solution.withSet(nums)

    def withSort(nums):
        nums.sort()
        high = len(nums)-1
        low = 0

        while high > low and nums[high] > 0:
            while -nums[low] > nums[high]:
                low += 1
            if high > low and -nums[low]==nums[high]:
                return nums[high]
            high -= 1
        return -1

    def withSet(nums):

        # one pass is better than two
        check = set()
        ret = -1
        for n in nums:            
            if -n in check:
                ret = max(ret, abs(n))
            check.add(n)

        # two passes
        #check = set(nums)
        #ret = -1
        #for n in nums:
        #    if -n in check:
        #        ret = max(ret, n)
        
        return ret
