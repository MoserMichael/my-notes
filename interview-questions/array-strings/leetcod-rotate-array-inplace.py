# 189. Rotate Array
# Medium
#Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
#
# 
#
#Example 1:
#
#Input: nums = [1,2,3,4,5,6,7], k = 3
#Output: [5,6,7,1,2,3,4]
#Explanation:
#rotate 1 steps to the right: [7,1,2,3,4,5,6]
#rotate 2 steps to the right: [6,7,1,2,3,4,5]
#rotate 3 steps to the right: [5,6,7,1,2,3,4]
#
#Example 2:
#
#Input: nums = [-1,-100,3,99], k = 2
#Output: [3,99,-1,-100]
#Explanation: 
#rotate 1 steps to the right: [99,-1,-100,3]
#rotate 2 steps to the right: [3,99,-1,-100]
#
# 
#
#Constraints:
#
#    1 <= nums.length <= 105
#    -231 <= nums[i] <= 231 - 1
#    0 <= k <= 105
#
# 
#
#Follow up:
#
#    Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
#    Could you do it in-place with O(1) extra space?
#


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        if k == 0:
            return
        k = k % len(nums)
        #Solution.rotateCopy(nums, k)
        #Solution.rotateCoppyBufferK(nums, k)
        Solution.rotateInplace(nums, k)

    @staticmethod
    def rotateInplace(nums, k):
        rndIdx = -1
        copyCount = 0

        while True:
            rndIdx += 1
            idx = rndIdx
            prev = nums[idx]

            while True:
                next_idx = (idx + k) % len(nums)

                next_prev = nums[next_idx]
                nums[next_idx] = prev

                prev = next_prev

                copyCount += 1
                if copyCount == len(nums):
                    return

                if next_idx == rndIdx:
                    break
                idx = next_idx



    @staticmethod
    def rotateCoppyBufferK(nums, k):
        buffer = [None] * k

        idx_two = 0
        for idx in range(len(nums)-k, len(nums)):
            buffer[idx_two] = nums[idx]
            idx_two += 1

        for idx in range(len(nums)-1, k-1, -1):
            nums[idx] = nums[idx-k]

        for idx in range(0, k):
            nums[idx] = buffer[idx]
        #print(f"nums {nums} buffer: {buffer}")


    @staticmethod
    def rotateCopy(nums, k):
        copy =  nums.copy()

        for idx in range(0, len(nums)):
            idx_two = idx - k
            if idx_two < 0:
                idx_two = len(nums) + idx_two
            copy[idx] = nums[idx_two]

        for idx in range(0, len(nums)):
             nums[idx] = copy[idx]


