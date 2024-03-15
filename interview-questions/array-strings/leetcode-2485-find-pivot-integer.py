# 2485. Find the Pivot Integer
# Easy
#    Given a positive integer n, find the pivot integer x such that:
#
#        The sum of all elements between 1 and x inclusively equals the sum of all elements between x and n inclusively.
#
#    Return the pivot integer x. If no such integer exists, return -1. It is guaranteed that there will be at most one pivot index for the given input.
#
#
#
#    Example 1:
#
#    Input: n = 8
#    Output: 6
#    Explanation: 6 is the pivot integer since: 1 + 2 + 3 + 4 + 5 + 6 = 6 + 7 + 8 = 21.
#
#    Example 2:
#
#    Input: n = 1
#    Output: 1
#    Explanation: 1 is the pivot integer since: 1 = 1.
#
#    Example 3:
#
#    Input: n = 4
#    Output: -1
#    Explanation: It can be proved that no such integer exist.
#
#
#
#    Constraints:
#
#        1 <= n <= 1000
#


class Solution:
    def pivotInteger(self, n: int) -> int:
        low = 1
        high = n

        hp = n * (n+1) // 2

        while low <= high:
            mid = (low + high) // 2
            low_p = mid * (mid+1) // 2
            high_p = hp  - low_p + mid

            #print(f"{low}..{mid}..{high} | {low_p} {high_p} {hp}")

            if low_p == high_p:
                return mid
            if low_p < high_p:
                low = mid+1
            else:
                high = mid-1
        return -1

