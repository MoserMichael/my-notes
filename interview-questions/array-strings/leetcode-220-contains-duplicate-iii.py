# 220. Contains Duplicate III
# Hard
#    You are given an integer array nums and two integers indexDiff and valueDiff.
#
#    Find a pair of indices (i, j) such that:
#
#        i != j,
#        abs(i - j) <= indexDiff.
#        abs(nums[i] - nums[j]) <= valueDiff, and
#
#    Return true if such pair exists or false otherwise.
#
#
#
#    Example 1:
#
#    Input: nums = [1,2,3,1], indexDiff = 3, valueDiff = 0
#    Output: true
#    Explanation: We can choose (i, j) = (0, 3).
#    We satisfy the three conditions:
#    i != j --> 0 != 3
#    abs(i - j) <= indexDiff --> abs(0 - 3) <= 3
#    abs(nums[i] - nums[j]) <= valueDiff --> abs(1 - 1) <= 0
#
#    Example 2:
#
#    Input: nums = [1,5,9,1,5,9], indexDiff = 2, valueDiff = 3
#    Output: false
#    Explanation: After trying all the possible pairs (i, j), we cannot satisfy the three conditions, so we return false.
#
#
#
#    Constraints:
#
#        2 <= nums.length <= 105
#        -109 <= nums[i] <= 109
#        1 <= indexDiff <= nums.length
#        0 <= valueDiff <= 109
#



class Entry:
    def __init__(self, value):
        self.value = value
        self.sorted_idx = -1

    def __repr__(self):
        return f"(val: {self.value} sorted_idx {self.sorted_idx})"

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:

        sorted_entry, val_to_entry = Solution.prepare(nums)
        value_to_last_occur = {}


        for idx, val_at_idx in enumerate(nums):

            val_at_idx = nums[idx]
            sorted_idx = val_to_entry[ idx ].sorted_idx

            max_idx = -1
            j = sorted_idx
            while j < len(nums):

                s_val = sorted_entry[j].value

                if abs(s_val - val_at_idx) > valueDiff:
                    break

                if s_val in value_to_last_occur:
                    max_idx = max(max_idx, value_to_last_occur[s_val])

                j += 1

            j = sorted_idx - 1
            while j >= 0:

                s_val = sorted_entry[j].value

                if abs(s_val - val_at_idx) > valueDiff:
                    break

                if s_val in value_to_last_occur:
                    max_idx = max(max_idx, value_to_last_occur[s_val])

                j -= 1

            if max_idx != -1 and idx - max_idx <= indexDiff:
                return True

            value_to_last_occur[ val_at_idx ] = idx

        return False


    def prepare(nums):
        val_to_entry = []
        sorted_entry = []

        for idx in range(0, len(nums)):
            e = Entry(nums[idx])

            val_to_entry.append(e)
            sorted_entry.append(e)

        sorted_entry.sort(key=lambda e : e.value)

        for idx in range(0, len(sorted_entry)):
            sorted_entry[idx].sorted_idx = idx

        return sorted_entry, val_to_entry
