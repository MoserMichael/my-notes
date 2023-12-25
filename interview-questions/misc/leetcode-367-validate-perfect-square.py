# 367. Valid Perfect Square
# Easy
#
#    Given a positive integer num, return true if num is a perfect square or false otherwise.
#
#    A perfect square is an integer that is the square of an integer. In other words, it is the product of some integer with itself.
#
#    You must not use any built-in library function, such as sqrt.
#
#
#
#    Example 1:
#
#    Input: num = 16
#    Output: true
#    Explanation: We return true because 4 * 4 = 16 and 4 is an integer.
#
#    Example 2:
#
#    Input: num = 14
#    Output: false
#    Explanation: We return false because 3.742 * 3.742 = 14 and 3.742 is not an integer.
#
#
#
#    Constraints:
#
#        1 <= num <= 231 - 1
#



class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        #return Solution.slow(num)
        return Solution.fast(num)

    def slow(n):
        for num in range(1,n+1):
            sq = num * num
            if sq == n:
                return True
            if sq > n:
                 return False
        return None

    def fast(num):
        low = 0
        high = num

        while low <= high:
            mid = (low + high) // 2

            if mid * mid == num:
                return True

            if mid * mid > num:
                prev = (mid-1) * (mid-1)
                if prev == num:
                    return True
                if prev > num:
                    high = mid - 1
                else:
                    return False
            else:
                low = mid+1

