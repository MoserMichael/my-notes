# 128. Longest Consecutive Sequence
# Medium
#Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
#
#You must write an algorithm that runs in O(n) time.
#
# 
#
#Example 1:
#
#Input: nums = [100,4,200,1,3,2]
#Output: 4
#Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
#
#Example 2:
#
#Input: nums = [0,3,7,2,5,8,4,6,0,1]
#Output: 9
#
# 
#
#Constraints:
#
#    0 <= nums.length <= 105
#    -109 <= nums[i] <= 109
#


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #return Solution.not_good(nums)
        return Solution.mergeIt(nums)


    @staticmethod
    def mergeIt(nums):
        low_to_high = {}
        high_to_low = {}

        for low in nums:
            high = low_to_high.get(low)
            if high is None:
                high = low+1
            else:
                assert high_to_low[high] == low

            r, h = Solution.mergeHigh(low, high, low_to_high, high_to_low)
            if not r:
                if high == low+1 and high not in high_to_low:
                    high_to_low[ high ] = low
                    low_to_high[ low ] = high
            else:
                high = h

            if low in low_to_high:
                Solution.mergeLow(low, high, low_to_high, high_to_low)


        max_range = 0
        for low, high in low_to_high.items():
            cur_range = high - low
            if cur_range > max_range:
                max_range = cur_range

        return max_range


    def mergeLow(low, high, low_to_high, high_to_low):

        assert len(low_to_high) == len(high_to_low)

        low_idx = high_to_low.get(low)
        if low_idx is not None:
            assert low_to_high[low_idx] == low
            low_to_high[low_idx] = high
            high_to_low.pop(low)
            low_to_high.pop(low)
            high_to_low[high] = low_idx

            assert len(low_to_high) == len(high_to_low)

    def mergeHigh(low, high, low_to_high, high_to_low):
        assert len(low_to_high) == len(high_to_low)

        high_idx = low_to_high.get(high)
        if high_idx is not None:
            assert high_to_low[ high_idx ] == high
            high_to_low[high_idx] = low
            low_to_high.pop(high)
            low_to_high[low] = high_idx

            assert len(low_to_high) == len(high_to_low)

            return True, high_idx
        return False, -1


    @staticmethod
    def not_good(nums):
        if len(nums) == 0:
            return 0

        nums.sort()

        longest_run = 1
        current_run = 1

        last = nums[0]
        idx = 1

        while idx < len(nums):

            if last == nums[idx]:
                idx += 1
                continue

            if last + 1 == nums[idx]: # or last == nums[idx]:
                current_run += 1
                if current_run > longest_run:
                    longest_run = current_run
            else:
                current_run = 1

            last = nums[idx]
            idx += 1

        #print(f"sorted {nums}")
        return longest_run



