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


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return Solution.fast(n)
        #return Solution.slow(n)

    def fast(n):
        if n <=0:
            return False

        # if 2 ^ 3  ==  1000
        # if (2 ^ 3) - 1 == 111
        return n & (n-1) == 0

    def slow(n):
        if n == 0:
            return False
        if n < 0:
            return False

        while True:
            if n == 1:
                return True
            if n & 1 != 0:
                return False
            n = n // 2


