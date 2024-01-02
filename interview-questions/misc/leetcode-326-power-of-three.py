# 326. Power of Three
# Easy
#
#    Given an integer n, return true if it is a power of three. Otherwise, return false.
#
#    An integer n is a power of three, if there exists an integer x such that n == 3x.
#
#
#
#    Example 1:
#
#    Input: n = 27
#    Output: true
#    Explanation: 27 = 33
#
#    Example 2:
#
#    Input: n = 0
#    Output: false
#    Explanation: There is no x where 3x = 0.
#
#    Example 3:
#
#    Input: n = -1
#    Output: false
#    Explanation: There is no x where 3x = (-1).
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


#    Intuition
#
#    iterative: compute the power of three, untill reaching target value (slowest option)
#
#    recursion: divide the input number by three, until reaching 1, if at any stage the remainder is not zero, then that's not a power of three
#
#    For binary search: start with the base three logarithm of the maximum input value, which is twenty.
#
#    The question of "Could you solve it without loops/recursion?". You can't solve this problem by checking the expression exp(3, log(n, 3)) == n ; the reason is that the computation of the logarithm gives a floating point number, and floating point numbers are just an approximation, so that this check will result in many errors.
#

import math

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        #return Solution.lib(n)
        return Solution.binsearch(n)
        #return Solution.rec(n)
        #return Solution.noRec(n)

    # that won't work - floating point numbers are approximate.
    def lib(n):
        if n <= 0:
            return False
        if n == 1:
            return True
        log_res = math.log(n, 3)
        return  float(n) == math.pow(3, int(log_res))

    # should be fastes
    def binsearch(n):
        if n <= 0:
            return False
        if n == 1:
            return True

        low = 1
        # 20 is math.log( 2<<31 - 1, 3)
        high = min(20,n//2)
        while low <= high:

            mid = (low+high)//2
            p = 3 ** mid

            if p == n:
                return True
            if p < n:
                low = mid+1
            else:
                high=mid-1

        return False

    # the recursive solution should be faster - it can stop halfway through the recursion, if the remainder is not zero.
    def rec(n):
        if n <= 0:
            return False
        if n == 1:
            return True
        if n % 3 != 0:
            return False
        return Solution.rec(n // 3)

    def noRec(n):
        if n < 1:
            return False
        m = 1
        while True:
            if m == n:
                return True
            if m > n:
                return False
            m = m * 3


