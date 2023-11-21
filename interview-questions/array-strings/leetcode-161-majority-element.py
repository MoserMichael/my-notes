# 169. Majority Element
# Easy
#Given an array nums of size n, return the majority element.
#
#The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
#
# 
#
#Example 1:
#
#Input: nums = [3,2,3]
#Output: 3
#
#Example 2:
#
#Input: nums = [2,2,1,1,1,2,2]
#Output: 2
#
# 
#
#Constraints:
#
#    n == nums.length
#    1 <= n <= 5 * 104
#    -109 <= nums[i] <= 109
#
# 
#Follow-up: Could you solve the problem in linear time and in O(1) space?
#

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #return Solution.withMap(nums)
        return Solution.boyer_moore_majority_alg(nums)

    @staticmethod
    def boyer_moore_majority_alg(nums):

        if len(nums) == 0:
            return -1

        count = 0
        elm = -1

        for num in nums:
            if count == 0:
                count = 1
                elm = num
            elif num == elm:
                count += 1
            else:
                count -= 1

        count = 0
        for num in nums:
            if num == elm:
                count += 1

        if count > len(nums)/2:
            return elm

        return -1

    @staticmethod
    def withMap(nums):
        countMap={}
        majority = 0
        majorityCount = 0

        for n in nums:
            if n in countMap:
                countMap[n] += 1
            else:
                countMap[n] = 1
            if majorityCount < countMap[n]:
                majorityCount = countMap[n]
                majority = n

        if majorityCount > len(nums)/2:
            return majority
        return -1

