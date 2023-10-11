# 9. Palindrome Number
# Easy
#Given an integer x, return true if x is a
#palindrome
#, and false otherwise.
#
#
#
#Example 1:
#
#Input: x = 121
#Output: true
#Explanation: 121 reads as 121 from left to right and from right to left.
#
#Example 2:
#
#Input: x = -121
#Output: false
#Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
#
#Example 3:
#
#Input: x = 10
#Output: false
#Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
#
#
#
#Constraints:
#
#    -231 <= x <= 231 - 1
#


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        ret = []
        while x > 0:
            num = x % 10
            ret.append(num)
            x = x // 10

        if len(ret) == 1:
            return True

        low = 0
        high = len(ret) - 1
        while low < high:
            if ret[low] != ret[high]:
                return False
            low += 1
            high -= 1
        
        return True
        
