# 41. First Missing Positive
# Hard
#    Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.
#
#    You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.
#
#     
#
#    Example 1:
#
#    Input: nums = [1,2,0]
#    Output: 3
#    Explanation: The numbers in the range [1,2] are all in the array.
#
#    Example 2:
#
#    Input: nums = [3,4,-1,1]
#    Output: 2
#    Explanation: 1 is in the array but 2 is missing.
#
#    Example 3:
#
#    Input: nums = [7,8,9,11,12]
#    Output: 1
#    Explanation: The smallest positive integer 1 is missing.
#
#     
#
#    Constraints:
#
#        1 <= nums.length <= 105
#        -231 <= nums[i] <= 231 - 1
#


import math
import collections

class Solution:

    def firstMissingPositive(self, nums: List[int]) -> int:
        c = set(filter(lambda val : val > 0, nums))

        n = 1
        while True:
            if not n in c:
                return n
            n += 1

    def notLinear(nums):

        c = collections.Counter(filter(lambda val : val > 0, nums))
        minval = reduce(lambda prev, cur: cur if cur < prev else prev, filter(lambda val : val > 0, nums), math.inf)
        maxval = reduce(lambda prev, cur: cur if cur > prev else prev, filter(lambda val : val > 0, nums), 0)

        print(minval, maxval, len(c), c)
        if minval>1:
            return 1
        if minval + len(c)-1 == maxval:
            return maxval+1

        sortedKeys = sorted(filter(lambda val : val > 0, c.keys()))
        #print(sortedKeys)

        low,high = 0, len(sortedKeys)-1
        while True:
            if high-low <= 1:
                return sortedKeys[low]+1
            mid=(low+high)//2
            #print(low,mid,high)
            if sortedKeys[mid]-sortedKeys[low] > (mid-low):
                high = mid
            else:
                low = mid



    def tooslow(nums):
        last = 0
        while True:
            small = math.inf
            for n in nums:
                if n > last and n < small:
                    small = n

            if small == math.inf or small > last+1:
                return last+1
            last = small

