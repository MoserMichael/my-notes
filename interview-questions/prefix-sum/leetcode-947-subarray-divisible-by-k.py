# 974. Subarray Sums Divisible by K
# Medium
#Given an integer array nums and an integer k, return the number of non-empty subarrays that have a sum divisible by k.
#
#A subarray is a contiguous part of an array.
#
#
#
#Example 1:
#
#Input: nums = [4,5,0,-2,-3,1], k = 5
#Output: 7
#Explanation: There are 7 subarrays with a sum divisible by k = 5:
#[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
#
#Example 2:
#
#Input: nums = [5], k = 9
#Output: 0
#
#
#
#Constraints:
#
#    1 <= nums.length <= 3 * 104
#    -104 <= nums[i] <= 104
#    2 <= k <= 104
#
#


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_map = defaultdict(int)

        sm = 0
        for idx in range(len(nums)):
            sm += nums[idx]
            md = sm % k

            prefix_map[md] += 1

        print(prefix_map)
        ret = prefix_map[0]


        for k,v in prefix_map.items():
            if v < 2:
                continue
            ret += ((v-1)*v)//2

        return ret
