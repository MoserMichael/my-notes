# 42. Trapping Rain Water
# Hard
#
#    Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
#
#
#
#    Example 1:
#
#    Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
#    Output: 6
#    Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
#
#    Example 2:
#
#    Input: height = [4,2,0,3,2,5]
#    Output: 9
#
#
#
#    Constraints:
#
#        n == height.length
#        1 <= n <= 2 * 104
#        0 <= height[i] <= 105
#

# Faster solutions don't use a stack, they have left,right pointer, where right points to current position and left to the matching level in the array.

class Solution:
    def trap(self, arr: List[int]) -> int:
        idx = 0

        for idx, val in enumerate(arr):
            if val != 0:
                break

        if idx == len(arr):
            return 0

        stk = [ (arr[idx], idx) ]
        ret = 0

        nxt = idx+1
        while nxt < len(arr):

            prev_height = 0
            if arr[nxt] != 0:
                while len(stk) != 0:
                    do_break = False
                    if arr[nxt] < stk[-1][0]:
                        entry = stk[-1]
                        ret += max( (nxt - entry[1] - 1) * (arr[nxt]-prev_height), 0)
                        do_break = True
                    else:
                        entry = stk.pop()
                        ret += max( (nxt - entry[1] - 1) * (entry[0]-prev_height), 0)

                    prev_height = entry[0]
                    if do_break:
                        break


            if arr[nxt] > 0:
                stk.append( (arr[nxt], nxt) )

            nxt += 1

        return ret



