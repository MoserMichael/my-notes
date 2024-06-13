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


#    ## two pointer
#
#    counter `low` for the range `nums[0:low]` that is set with zero values
#    counter `high` for the range `nums[high:]` that will be set with two values.
#
#    determine these two values in the following loop, note that the zeros are also set, as the low pointer advances.
#
#    <pre><code>
#    low, high = 0, len(nums)-1
#    for val in nums:
#        if val == 0:
#            nums[low] = 0
#            low += 1
#        elif val == 2:
#            high -= 1
#    </code></pre>
#
#    Next, set all values between `low` and `high` to one and all remaining values to two.
#
#    ## two liner based on count
#
#    Count the occurances of zero, ones and twos.
#    The resulting array is of the form `[0]*cnt[0]+[1]*cnt[1]+[2]*cnt[2]`
#
#    Now copy this array in place into the argument array.
#
#    `for idx, val in enumerate([0]*cnt[0]+[1]*cnt[1]+[2]*cnt[2]): nums[idx]=val`
#
# Code

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        low, high = 0, len(nums)-1
        for val in nums:
            if val == 0:
                nums[low] = 0
                low += 1
            elif val == 2:
                high -= 1

        while low <= high:
            nums[low] = 1
            low += 1
        while low < len(nums):
            nums[low] = 2
            low += 1

    def oneLiner(nums):
        cnt = Counter(nums)
        for idx, val in enumerate([0]*cnt[0]+[1]*cnt[1]+[2]*cnt[2]): nums[idx]=val


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


