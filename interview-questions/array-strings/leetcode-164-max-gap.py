# 164. Maximum Gap
# Medium
#Given an integer array nums, return the maximum difference between two successive elements in its sorted form. If the array contains less than two elements, return 0.
#
#You must write an algorithm that runs in linear time and uses linear extra space.
#
# 
#
#Example 1:
#
#Input: nums = [3,6,9,1]
#Output: 3
#Explanation: The sorted form of the array is [1,3,6,9], either (3,6) or (6,9) has the maximum difference 3.
#
#Example 2:
#
#Input: nums = [10]
#Output: 0
#Explanation: The array contains less than 2 elements, therefore return 0.
#
# 
#
#Constraints:
#
#    1 <= nums.length <= 105
#    0 <= nums[i] <= 109
#



class Solution:
    def maximumGap(self, nums: List[int]) -> int:

            if len(nums) < 2:
                return 0

            min_val = min(nums)
            max_val = max(nums)

            if min_val == max_val:
                return 0

            bsize = max(1, (max_val - min_val) // len(nums))
            bnum = (max_val - min_val) // bsize
            buck =  [ [] for _ in range(bnum+1) ]

            for n in nums:
                idx = (n - min_val) // bsize
                buck[idx].append(n)

            prev = -1
            ret = 0

            for b in buck:
                if len(b) != 0:
                    b.sort()
                    for n in b:
                        if prev == -1:
                            prev = n
                        else:
                            ret = max(ret, n - prev)
                            prev = n

            return ret


