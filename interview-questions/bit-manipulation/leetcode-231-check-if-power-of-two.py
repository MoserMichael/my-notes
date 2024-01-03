# 231. Power of Two
# Easy
#
#    Given an integer n, return true if it is a power of two. Otherwise, return false.
#
#    An integer n is a power of two, if there exists an integer x such that n == 2x.
#
#
#
#    Example 1:
#
#    Input: n = 1
#    Output: true
#    Explanation: 20 = 1
#
#    Example 2:
#
#    Input: n = 16
#    Output: true
#    Explanation: 24 = 16
#
#    Example 3:
#
#    Input: n = 3
#    Output: false
#
#
#
#    Constraints:
#
#        -231 <= n <= 231 - 1
#
#
#    Follow up: Could you solve it without loops/recursion?
#



# here they have other tricks as well:
# https://en.wikipedia.org/wiki/Hamming_weight

class Solution:
    def hammingWeight(self, n: int) -> int:
        #return Solution.oneBit(n)
        return Solution.bitOp(n)

    def bitOp(n):
        ret = 0
        while n != 0:
            # n & (n-1)

            # he bitwise AND of x with x − 1 differs from x only in zeroing out the least significant nonzero bit: subtracting 1 changes the rightmost string of 0s to 1s, and changes the rightmost 1 to a 0

            n = n & (n-1)
            ret += 1
        return ret


    def oneBit(n):
        ret = 0
        while n != 0:
            ret += n & 1

            #if is a big slow down!!!
            #if n & 1:
            #  ret += 1

            n >>=1
        return ret


