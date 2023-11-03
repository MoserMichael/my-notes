#81. Search in Rotated Sorted Array II
#Medium
#
#    There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).
#
#    Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].
#
#    Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.
#
#    You must decrease the overall operation steps as much as possible.
#
#     
#
#    Example 1:
#
#    Input: nums = [2,5,6,0,0,1,2], target = 0
#    Output: true
#
#    Example 2:
#
#    Input: nums = [2,5,6,0,0,1,2], target = 3
#    Output: false
#



class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        first = nums[0]
        displace = Solution.imp(nums, 0, len(nums)-1, first)
        return Solution.searchMod(target, nums, displace, 0, len(nums)-1) != -1


    @staticmethod
    def searchMod(target, nums, displace, low, high):
        #print(f"{low}..{high}")
        if low > high:
            return -1
        mid = int( (low+high) / 2 )
        pos = (mid + displace) % len(nums)
        if nums[pos] == target:
            return pos
        if nums[pos] < target:
            return Solution.searchMod(target, nums, displace, mid+1, high)
        return Solution.searchMod(target, nums, displace, low, mid-1)


    @staticmethod
    def imp(nums, low, high, first):
        if low > high:
            return 0
        mid = int( (low+high)/2 )

        cmp=0
        if mid > 0:
            cmp=1
            if nums[mid]<nums[mid-1]:
                return mid

        if mid < len(nums)-1:
            cmp=1
            if nums[mid+1]<nums[mid]:
                return mid + 1

        if cmp==0:
            return 0


        if nums[low] == nums[high]:
            rt = Solution.imp(nums, low, mid-1, first)
            if rt != 0:
                return rt
            return Solution.imp(nums, mid+1, high, first)


        if nums[mid] >= first:
            return Solution.imp(nums, mid+1, high, first)
        return Solution.imp(nums, low, mid-1, first)


