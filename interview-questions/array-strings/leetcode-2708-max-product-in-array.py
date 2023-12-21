# 2708. Maximum Strength of a Group
# Medium
#
#    You are given a 0-indexed integer array nums representing the score of students in an exam. The teacher would like to form one non-empty group of students with maximal strength, where the strength of a group of students of indices i0, i1, i2, ... , ik is defined as nums[i0] * nums[i1] * nums[i2] * ... * nums[ik​].
#
#    Return the maximum strength of a group the teacher can create.
#
#     
#
#    Example 1:
#
#    Input: nums = [3,-1,-5,2,5,-9]
#    Output: 1350
#    Explanation: One way to form a group of maximal strength is to group the students at indices [0,2,3,4,5]. Their strength is 3 * (-5) * 2 * 5 * (-9) = 1350, which we can show is optimal.
#
#    Example 2:
#
#    Input: nums = [-4,-5,-4]
#    Output: 20
#    Explanation: Group the students at indices [0, 1] . Then, we’ll have a resulting strength of 20. We cannot achieve greater strength.
#
#     
#
#    Constraints:
#
#        1 <= nums.length <= 13
#        -9 <= nums[i] <= 9
#


## Intuition
#Two solutions:
#- ```Solution.withSort``` solution that firsts sorts all numbers in ascending order, next stage: add the product of all positive numbers to the result, then add the product of all smallest pairs of negative numbers. This solution is easy to code and to understand.
#- ```Solution.noSort```, there is a O(n) case (don't do it like this - there are easier solutions... !!!),  The solution:
#  - one pass over the input: compute the product of all positive numbers,
#  - compute the product of all negative numbers, count the number of -1 instances, and the largest negative number
#  - if the maximum number is positive: (easy case)
#      - if positive * negative is positive - go for it
#      - if we have minus ones, then turn the negative value of negtative product into a positive one, positive * - negative - go for it.
#      - else return positive product * negative product // maximum negative number
#  - if the maximum number is negative, messy stuff. see how it works.
#
## Approach
#
## Complexity
#- Time complexity:
# O(n) in one pass
# O(nlogn) the easier solution that needs sort
#

import math

class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        return Solution.noSort(nums)
        #return Solution.withSort(nums)

    # FUCK THE EDGE CASES
    def noSort(nums):

        pos_prod = 1
        neg_prod = 1
        minus_one = 0
        neg_prod_count = 0
        max_neg = -math.inf

        max_num = -math.inf
        min_num = math.inf

        for n in nums:
            max_num = max(max_num, n)
            min_num = min(min_num, n)

            if n >= 1:
                pos_prod *= n
            elif n < -1:
                neg_prod *= n
                neg_prod_count += 1
                max_neg = max(max_neg, n)
            elif n== -1:
                minus_one += 1

        if len(nums) == 1:
            return nums[0]

        if max_num <= 0:
            if neg_prod_count > 0:
                if neg_prod > 0:
                    return neg_prod
                if minus_one > 0:
                    return -neg_prod
                if neg_prod_count > 1:
                    return neg_prod // max_neg

            if minus_one > 0:
                if neg_prod_count > 0:
                    return - neg_prod
                if minus_one > 1:
                    return 1
            return max_num


        if max_num >= 1:
            if neg_prod > 0:
                return pos_prod * neg_prod
            if minus_one > 0:
                return -pos_prod * neg_prod

            return pos_prod * neg_prod // max_neg

        #[-1..0]
        return max(max_num, 1 if minus_one > 1 else min_num)

    def withSort(nums):
        nums.sort()
        #nums=sorted(nums)

        prod=1
        ops=0

        idx = len(nums)-1
        while idx >= 0:
           if nums[idx]<=1:
               break
           prod *= nums[idx]
           ops += 1
           idx -= 1

        idx=0
        while idx < len(nums)-1:
            if nums[idx] >-1 or nums[idx+1] > -1:
                break
            prod *= nums[idx] * nums[idx+1]
            idx += 2
            ops += 1

        if ops == 0:
            return max(nums)
        return prod





