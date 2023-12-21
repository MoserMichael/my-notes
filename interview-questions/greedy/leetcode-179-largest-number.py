# 179. Largest Number
# Medium
#
#    Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.
#
#    Since the result may be very large, so you need to return a string instead of an integer.
#
#
#
#    Example 1:
#
#    Input: nums = [10,2]
#    Output: "210"
#
#    Example 2:
#
#    Input: nums = [3,30,34,5,9]
#    Output: "9534330"
#
#
#
#    Constraints:
#
#        1 <= nums.length <= 100
#        0 <= nums[i] <= 109
#



import functools

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums=sorted(nums, key=functools.cmp_to_key(Solution.cmp))
        return str( int( "".join(map(str,nums)) ) )

    def cmp(a,b):
        na = int( str(a)+str(b) )
        nb = int( str(b)+str(a) )

        if na > nb:
            return -1
        if nb < na:
            return 1

        return 0

