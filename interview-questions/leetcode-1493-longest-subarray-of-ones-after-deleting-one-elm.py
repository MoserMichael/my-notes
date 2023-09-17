# 1493. Longest Subarray of 1's After Deleting One Element
# Medium
#Given a binary array nums, you should delete one element from it.
#
#Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.
#
#
#
#Example 1:
#
#Input: nums = [1,1,0,1]
#Output: 3
#Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
#
#Example 2:
#
#Input: nums = [0,1,1,1,0,1,1,0,1]
#Output: 5
#Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].
#
#Example 3:
#
#Input: nums = [1,1,1]
#Output: 2
#Explanation: You must delete one element.
#
#
#
#Constraints:
#
#    1 <= nums.length <= 105
#    nums[i] is either 0 or 1.
#




class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        i=0
        blocks=[]

        while i < len(nums):
            j=i+1
            
            while j < len(nums) and nums[i]==nums[j]:
                j+=1
            blockLen=j-i            
            if nums[i]:
                blocks.append(blockLen)
            else:
                blocks.append(-blockLen)
            i=j


        if len(blocks) == 1 and blocks[0] > 0:
            return blocks[0] -1

        maxMergedLen = 0
        for idx in range(0,len(blocks)):
            if blocks[idx] == -1: 
                mergedLen = 0
                if idx > 0:
                    mergedLen += blocks[idx-1]
                if (idx+1) < len(blocks):
                    mergedLen += blocks[idx+1]  

                maxMergedLen = max(maxMergedLen, mergedLen)

            if blocks[idx] < -1:     
                if idx > 0:
                    maxMergedLen = max(maxMergedLen, blocks[idx-1])
                if (idx+1) < len(blocks):
                    maxMergedLen = max(maxMergedLen, blocks[idx+1])


        return maxMergedLen
