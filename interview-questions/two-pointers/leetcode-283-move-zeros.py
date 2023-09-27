# 283. Move Zeroes
# Easy
#Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
#
#Note that you must do this in-place without making a copy of the array.
#
#
#
#Example 1:
#
#Input: nums = [0,1,0,3,12]
#Output: [1,3,12,0,0]
#
#Example 2:
#
#Input: nums = [0]
#Output: [0]
#

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        low=0
        high=0

        while high < len(nums):
            if nums[high] !=0:
                nums[low] = nums[high]
                low += 1
            high += 1

        while low < len(nums):
            nums[low] = 0
            low += 1
        
