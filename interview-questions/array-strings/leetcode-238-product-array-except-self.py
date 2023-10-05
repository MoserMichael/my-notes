# 238. Product of Array Except Self
# Medium
#Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
#
#The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
#
#You must write an algorithm that runs in O(n) time and without using the division operation.
#
# 
#
#Example 1:
#
#Input: nums = [1,2,3,4]
#Output: [24,12,8,6]
#
#Example 2:
#
#Input: nums = [-1,1,0,-3,3]
#Output: [0,0,9,0,0]
#
# 
#
#Constraints:
#
#    2 <= nums.length <= 105
#    -30 <= nums[i] <= 30
#    The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
#
# 
#
#Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
#

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #return Solution.o_n_no_division(nums)
        return Solution.no_intermediate_arrays(nums)

    @staticmethod
    def no_intermediate_arrays(nums):
        left_prod = [0] * len(nums)

        cur_right_prod = cur_left_prod = 1

        res = [0] * len(nums)

        cur_left_prod = 1
        for idx in range(0, len(nums)):
            cur_left_prod *= nums[idx]
            res[idx] = cur_left_prod

        cur_right_prod = 1
        for idx in range(len(nums)-1, -1, -1):

            cur_left_prod = 1
            if idx > 0:
                cur_left_prod = res[idx-1]

            res[idx] = cur_left_prod * cur_right_prod
            cur_right_prod *= nums[idx]

        return res

    @staticmethod
    def o_n_no_division(nums):
        left_prod = [0] * len(nums)
        right_prod = [0] * len(nums)

        cur_right_prod = cur_left_prod = 1

        for idx in range(0, len(nums)):
            cur_left_prod *= nums[idx]
            left_prod[idx] = cur_left_prod

            right_idx = len(nums)-1-idx
            cur_right_prod *= nums[right_idx]
            right_prod[right_idx] = cur_right_prod

        res = []

        for idx in range(0, len(nums)):
            cur_left_prod=1
            if idx > 0:
                cur_left_prod=left_prod[idx-1]
            cur_right_prod=1
            if idx < len(nums)-1:
                cur_right_prod=right_prod[idx+1]

            #res[idx] = cur_left_prod * cur_right_prod
            res.append(cur_left_prod * cur_right_prod)

        return res


