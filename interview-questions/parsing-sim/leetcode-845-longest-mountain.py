# 845. Longest Mountain in Array
# Medium
#
#    You may recall that an array arr is a mountain array if and only if:
#
#        arr.length >= 3
#        There exists some index i (0-indexed) with 0 < i < arr.length - 1 such that:
#            arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
#            arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
#
#    Given an integer array arr, return the length of the longest subarray, which is a mountain. Return 0 if there is no mountain subarray.
#
#
#
#    Example 1:
#
#    Input: arr = [2,1,4,7,3,2,5]
#    Output: 5
#    Explanation: The largest mountain is [1,4,7,3,2] which has length 5.
#
#    Example 2:
#
#    Input: arr = [2,2,2]
#    Output: 0
#    Explanation: There is no mountain.
#
#
#
#    Constraints:
#
#        1 <= arr.length <= 104
#        0 <= arr[i] <= 104
#
#
#
#    Follow up:
#
#        Can you solve it using only one pass?
#        Can you solve it in O(1) space?
#
#




class Solution:

    STATE_NO_MOUNTAIN = 0
    MOUNTAIN_UP = 1
    MOUNTAIN_DOWN=2

    def longestMountain(self, arr: List[int]) -> int:
        state = Solution.STATE_NO_MOUNTAIN

        ret = 0

        i = 1
        while i < len(arr):
            if state == Solution.STATE_NO_MOUNTAIN:
                if arr[i] > arr[i-1]:
                    start = i-1
                    state = Solution.MOUNTAIN_UP
            elif state == Solution.MOUNTAIN_UP:
                if arr[i] == arr[i-1]:
                    state = Solution.STATE_NO_MOUNTAIN
                elif arr[i-1] > arr[i]:
                    state = Solution.MOUNTAIN_DOWN
            else: # MOUNTAIN_DOWN
                if arr[i-1] <= arr[i]:
                    range_len = i - start
                    ret = max(ret, range_len)
                    state = Solution.STATE_NO_MOUNTAIN

                    # here is the trick
                    i -= 1
                    continue

            i += 1

        if state == Solution.MOUNTAIN_DOWN:
            range_len = i - start
            ret = max(ret, range_len)

        return ret


