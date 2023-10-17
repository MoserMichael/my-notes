# 219. Contains Duplicate II
# Easy
#Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
#
#
#
#Example 1:
#
#Input: nums = [1,2,3,1], k = 3
#Output: true
#
#Example 2:
#
#Input: nums = [1,0,1,1], k = 1
#Output: true
#
#Example 3:
#
#Input: nums = [1,2,3,1,2,3], k = 2
#Output: false
#
#
#
#Constraints:
#
#    1 <= nums.length <= 105
#    -109 <= nums[i] <= 109
#    0 <= k <= 105
#


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        num_to_pos = {}
        for idx in range(0, len(nums)):
            lst = num_to_pos.setdefault(nums[idx], [])
            lst.append(idx)

        for num, positions in num_to_pos.items():
            positions.sort()
            for idx in range(1, len(positions)):
                if positions[idx] - positions[idx-1] <= k:
                    return True

        return False

