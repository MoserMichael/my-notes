# 523. Continuous Subarray Sum
# Medium
#Given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.
#
#A good subarray is a subarray where:
#
#    its length is at least two, and
#    the sum of the elements of the subarray is a multiple of k.
#
#Note that:
#
#    A subarray is a contiguous part of the array.
#    An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.
#
#
#
#Example 1:
#
#Input: nums = [23,2,4,6,7], k = 6
#Output: true
#Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.
#
#Example 2:
#
#Input: nums = [23,2,6,4,7], k = 6
#Output: true
#Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42.
#42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.
#
#Example 3:
#
#Input: nums = [23,2,6,4,7], k = 13
#Output: false
#

#
## Intuition
#
#Need to check if the sum is divisable by `k` this means that division by modulo `k` must be equal to zero - `sum(nums[i:j]) % k == 0`
#
#This condition is met if there are two prefix sums (meaning sums of arrays starting with index zero) - `sum(nums[0:i]) % k == sum(nums[0:j]) % k` where `j-i > 1` - the last condition means that at least two elements formed the sum `nums[i:j]`.
#
#Now to check if there are any subarrays with at least two elements divisable by k:
#- maintain a map `prefix_map` that maps the sum modulo k of a prefix array to the position of the prefix array, example: for a subarray `nums[0:4]` with `sum(nums[0:4]) % k == 10`, add an entry `prefix_map[10] = 4` - note that the entry with the earliest index must be kept, if you get `sum(nums[0:5]) % k == 10` then do not overwrite the entry `prefix_map[10] = 4`
#
## Solution
#
#now check for a solution: loop on all indexes `idx` in `range(len(nums))` and compute the sum modulo `k` of `nums[0:idx]`
#
#<pre><code>sm = 0
#for idx in range(len(nums)):
#    sm += nums[idx]
#    md = sm % k
#<code></pre>
#
#Check if the modulo sum is equal to zero and index greater than one - in this case we have a solution, as `sum(nums[0:idx] % k == 0`.
#
#<pre><code>    if md == 0 and idx > 0:
#        return True
#<code></pre>
#
#Now the trick with the prefix map: if we already have a prefix with the same value modulo k, and it happened earlier than the last index, then we have a match. If this is a new sum modulo k value, then enter it into the prefix map
#
#
#<pre><code>    val = prefix_map.get(md)
#    if val is not None:
#        if val < idx-1:
#            return True
#    else:
#        prefix_map[md] = idx
#</code></pre>
#
#
#If no matches have been found then return false.
#
#


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix_map = {}

        sm = 0
        for idx in range(len(nums)):
            sm += nums[idx]
            md = sm % k
            if md == 0 and idx > 0:
                return True
            val = prefix_map.get(md)
            if val is not None:
                if val < idx-1:
                    return True
            else:
                prefix_map[md] = idx

        return False


