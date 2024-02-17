# 80. Remove Duplicates from Sorted Array II
# Medium
#
#    Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.
#
#    Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.
#
#    Return k after placing the final result in the first k slots of nums.
#
#    Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
#
#    Custom Judge:
#
#    The judge will test your solution with the following code:
#
#    int[] nums = [...]; // Input array
#    int[] expectedNums = [...]; // The expected answer with correct length
#
#    int k = removeDuplicates(nums); // Calls your implementation
#
#    assert k == expectedNums.length;
#    for (int i = 0; i < k; i++) {
#        assert nums[i] == expectedNums[i];
#    }
#
#    If all assertions pass, then your solution will be accepted.
#
#
#
#    Example 1:
#
#    Input: nums = [1,1,1,2,2,3]
#    Output: 5, nums = [1,1,2,2,3,_]
#    Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
#    It does not matter what you leave beyond the returned k (hence they are underscores).
#
#    Example 2:
#
#    Input: nums = [0,0,1,1,1,1,2,3,3]
#    Output: 7, nums = [0,0,1,1,2,3,3,_,_]
#    Explanation: Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.
#    It does not matter what you leave beyond the returned k (hence they are underscores).
#
#
#
#    Constraints:
#
#        1 <= nums.length <= 3 * 104
#        -104 <= nums[i] <= 104
#        nums is sorted in non-decreasing order.
#


#        # Intuition
#        two indexes move through the array, the slow index points at the area removed of duplicates, the fast index points at the next input number
#
#        # Approach
#        - check for duplicates: while the ```nums[fast]==nums[slow]``` - increment fast.
#        - copy the first repeating element
#        - advance slow to the next byte that has not been set,
#        - copy the current fast pointer to new slow location ```nums[slow] = nums[fast]```
#        - increment fast pointer to the next input number
#        # Complexity
#        - Time complexity:
#        $$O(n)$$ - one pass over the input
#
#        - Space complexity:
#        $$O(1)$$ - the solution does not require the addition of any collection, just scalars.
#
#        # Code
#        ```
#        class Solution:
#            def removeDuplicates(self, nums: List[int]) -> int:
#                if len(nums) < 2:
#                    return len(nums)
#
#                low = 0
#                high = 1
#                while high < len(nums):
#                    if nums[low] == nums[high]:
#                        # check for duplicates:
#                        while nums[low] == nums[high]:
#                            high += 1
#                            if high >= len(nums):
#                                break
#
#                        low+=1
#
#                        # copy the first repeating element
#                        nums[low] = nums[low-1]
#
#                        if high >= len(nums):
#                            return low+1
#
#                    # advance slow to the next byte that has not been set,
#                    low += 1
#                    if high > low:
#                        # copy the current fast pointer to new slow location
#                        nums[low] = nums[high]
#                    high += 1
#
#                return low+1
#
#
#
#        ```


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)

        low = 0
        high = 1
        while high < len(nums):
            if nums[low] == nums[high]:
                while nums[low] == nums[high]:
                    high += 1
                    if high >= len(nums):
                        break
                        #return low+1
                low+=1
                nums[low] = nums[low-1]
                if high >= len(nums):
                    return low+1

            low += 1
            if high > low:
                nums[low] = nums[high]
            high += 1

        return low+1



