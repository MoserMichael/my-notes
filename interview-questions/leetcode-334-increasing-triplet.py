#334. Increasing Triplet Subsequence
#Medium
#Companies
#
#Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.
#
# 
#
#Example 1:
#
#Input: nums = [1,2,3,4,5]
#Output: true
#Explanation: Any triplet where i < j < k is valid.
#
#Example 2:
#
#Input: nums = [5,4,3,2,1]
#Output: false
#Explanation: No triplet exists.
#
#Example 3:
#
#Input: nums = [2,1,5,0,4,6]
#Output: true
#Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.
#
# 
#
#Constraints:
#
#    1 <= nums.length <= 5 * 105
#    -231 <= nums[i] <= 231 - 1
#
# 
#Follow up: Could you implement a solution that runs in O(n) time complexity and O(1) space complexity?
#

import math

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        # run to long on big array with two values
        setVals=set()
        for n in nums:
            setVals.add(n)
        if len(setVals) < 3:
            return False

        return self.increasing(nums, -math.inf, -1, 3)

    def increasing(self, nums, prevMax, prevIdx, numLeft):
        if numLeft == 0:
            return True

        for i in range(prevIdx+1, len(nums)):
            if nums[i] > prevMax:
                if self.increasing( nums, nums[i], i, numLeft-1):
                    return True

        return False
        
