# 2529. Maximum Count of Positive Integer and Negative Integer
# Easy
#Given an array nums sorted in non-decreasing order, return the maximum between the number of positive integers and the number of negative integers.
#
#    In other words, if the number of positive integers in nums is pos and the number of negative integers is neg, then return the maximum of pos and neg.
#
#
#Note that 0 is neither positive nor negative.
#
#
#Example 1:
#
#
#Input: nums = [-2,-1,-1,1,2,3]
#
#Output: 3
#
#Explanation: There are 3 positive integers and 3 negative integers. The maximum count among them is 3.
#
#
#Example 2:
#
#Input: nums = [-3,-2,-1,0,0,1,2]
#
#Output: 3
#
#Explanation: There are 2 positive integers and 3 negative integers. The maximum count among them is 3.
#
#
#Example 3:
#
#Input: nums = [5,20,66,1314]
#
#Output: 4
#
#Explanation: There are 4 positive integers and 0 negative integers. The maximum count among them is 4.
#
#
#Constraints:
#
#    1 <= nums.length <= 2000
#
#    -2000 <= nums[i] <= 2000
#
#    nums is sorted in a non-decreasing order.
#
#
#Follow up: Can you solve it in O(log(n)) time complexity?
#

#    # Intuition
#
#
#
#    find the position of the last negative and first positive number via binary search. 
#
#    The trick is to take care of the situation when the mid point is equal to zero (when finding the first positive) or when the mid point is equal to the last element (when finding the last negative) - in these cases the find routines return -1.
#
#
#
#    # Complexity
#
#    - Time complexity:
#
#    $$O(log n)$$
#
#
#
#    - Space complexity:
#
#    $$O(log 1)$$
#
#
#
## Code
#
#```
#
class Solution:

    def maximumCount(self, nums: List[int]) -> int:

        last_neg = Solution.findLastNegative(nums) 

        first_pos = Solution.findFirstPositive(nums)



        if last_neg == -1:

            num_pos = 0

        else:

            num_pos = last_neg + 1



        if first_pos == -1:

            num_neg = 0

        else:

            num_neg = len(nums) - first_pos



        return max(num_pos, num_neg)



    # find position of nums[pos] < 0 and nums[pos+1] >= 0

    def findLastNegative(nums):

        

        low = 0

        first_high = high = len(nums)-1



        while low <= high:

            mid = (low + high) // 2

            if nums[mid] < 0:

                if mid == first_high or nums[mid+1] >= 0:

                    return mid

                low = mid + 1

            else:

                high = mid-1



        return -1



    #find position of num[pos] > 0 and num[pos-1] <= 0

    def findFirstPositive(nums):



        low = 0

        high = len(nums)-1



        while low <= high:

            mid = (low + high) // 2

            

            if nums[mid] > 0:

                if mid == 0 or nums[mid-1] <= 0:

                    return mid

                high = mid - 1

            else:

                low = mid + 1



        return -1

