# 7. Reverse Integer
# Medium
#Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
#
#Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
#
#
#
#Example 1:
#
#Input: x = 123
#Output: 321
#
#Example 2:
#
#Input: x = -123
#Output: -321
#
#Example 3:
#
#Input: x = 120
#Output: 21
#
#
#
#Constraints:
#
#    -231 <= x <= 231 - 1
#



class Solution:
    def reverse(self, x: int) -> int:

        sign = 1
        if x < 0:
            sign = -1
        x = abs(x)

        digits = []
        while x > 0:
            digits.append( x % 10)
            x //= 10

        power =  10 ** (len(digits) - 1)

        sum_num = 0
        for dig in digits:
            sum_num += power * dig
            power //= 10


        if not -pow(2, 31) < sum_num < (pow(2,31) - 1):
            return 0

        return sum_num * sign
