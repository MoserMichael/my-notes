# 75. Sort Colors
# Medium
#    Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
#
#    We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
#
#    You must solve this problem without using the library's sort function.
#
#
#
#    Example 1:
#
#    Input: nums = [2,0,2,1,1,0]
#    Output: [0,0,1,1,2,2]
#
#    Example 2:
#
#    Input: nums = [2,0,1]
#    Output: [0,1,2]
#
#
#
#    Constraints:
#
#        n == nums.length
#        1 <= n <= 300
#        nums[i] is either 0, 1, or 2.
#
#
#
#    Follow up: Could you come up with a one-pass algorithm using only constant extra space?
#

#
#    # Intuition
#
#    Count the number of zeros, ones and twos, set the elements to these values, according to their count.
#
#    # Approach
#    Do both in one and in two passes, with O(1) in memory:
#
#    - function sortColorsTwoPass
#    - Two passes: pass over the input and count the nunbmer of zeros, ones and twos.
#    - Second passes, if number of counted zeros is equal to n, set the first n elements to zero, if number of counted ones is m - set the next m elements to one, if number of counted zeros is equal to o, set the next o elements to two.
#
#    Now in one pass
#
#    - function sortColorsOnePass
#    - maintain count low_read=0 and high_read=len(nums-1), elements at these counters is read and the value of zeros,ones and twos at these indexes is counted.
#    - maintain index low_write=0 and high_write=len(nums)-1, while low_read < high_read
#       - while low_write is smaller than low_read and number of written zeros is smaller than the count of written zeroes, write another batch of zeros at low_write and increment the low_write value
#       - while high_write is larger than high_read, and number of twos is smaller than the count of written twos, write another batch of twos at high_write and decrement the value of high_write.
#    - after the end of loop, if low_read == high_read then count the current value at this index (otherwise we didn't count the last number.)
#    - write the remaining count of ones and twos, the rest of the number is written as one.
#
#    # Complexity
#    - Time complexity: O(n) - one pass over the input for the second solution (for low_write and high_write that follow low_read and high_read)
#
#    - Space complexity: O(1) - three counters are maintained.
#
#

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        return Solution.sortColorsOnePass(nums)
        #return Solution.sortColorsTwoPass(nums)

    def sortColorsOnePass(nums):
        if len(nums) == 0:
            return

        low_read = 0
        high_read = len(nums)-1

        low_write = 0
        high_write = len(nums)-1

        count = [0] * 3

        while low_read < high_read:
            count[ nums[low_read] ] += 1
            count[ nums[high_read] ] += 1

            while count[ 0 ] > low_write and low_write < low_read:
                nums[low_write] = 0
                low_write += 1

            while count[ 2 ] > (len(nums) - 1 - high_write) and high_write > high_read:
                nums[high_write] = 2
                high_write -= 1

            low_read += 1
            high_read -= 1

        if low_read == high_read:
            count[ nums[low_read] ] += 1


        while low_write < count[ 0 ]:
            nums[low_write] = 0
            low_write += 1

        while count[ 2 ] > (len(nums) - 1 - high_write):
            nums[high_write] = 2
            high_write -= 1

        while low_write <= high_write:
            nums[low_write] = 1
            low_write += 1

    def sortColorsTwoPass(nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0] * 3

        for num in nums:
            count[num] += 1

        idx = 0
        for idx_count in range(0, len(count)):
            num_repeat = count[idx_count]
            for i in range(0, num_repeat):
                nums[idx] = idx_count
                idx += 1

        return nums


