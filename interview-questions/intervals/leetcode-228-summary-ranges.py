# 228. Summary Ranges
# Easy
#You are given a sorted unique integer array nums.
#
#A range [a,b] is the set of all integers from a to b (inclusive).
#
#Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.
#
#Each range [a,b] in the list should be output as:
#
#    "a->b" if a != b
#    "a" if a == b
#
# 
#
#Example 1:
#
#Input: nums = [0,1,2,4,5,7]
#Output: ["0->2","4->5","7"]
#Explanation: The ranges are:
#[0,2] --> "0->2"
#[4,5] --> "4->5"
#[7,7] --> "7"
#
#Example 2:
#
#Input: nums = [0,2,3,4,6,8,9]
#Output: ["0","2->4","6","8->9"]
#Explanation: The ranges are:
#[0,0] --> "0"
#[2,4] --> "2->4"
#[6,6] --> "6"
#[8,9] --> "8->9"
#
# 
#
#Constraints:
#
#    0 <= nums.length <= 20
#    -231 <= nums[i] <= 231 - 1
#    All the values of nums are unique.
#    nums is sorted in ascending order.
#


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        if len(nums) == 0:
            return ""

        ret = []

        first=0
        last=1

        while last < len(nums):
            if nums[last] == nums[last-1] + 1:
                last += 1
            else:
                Solution.add(ret, first, last, nums)

                first = last
                last += 1

        Solution.add(ret, first, len(nums), nums)

        return ret

    def add(ret_arr, first, last, nums):
        if first + 1 == last:
            ret_arr.append(str(nums[first]))
        else:
            ret_arr.append(f"{nums[first]}->{nums[last-1]}")


