#1071. Greatest Common Divisor of Strings
#
#For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).
#
#Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.
#
# 
#
#Example 1:
#
#Input: str1 = "ABCABC", str2 = "ABC"
#Output: "ABC"
#
#Example 2:
#
#Input: str1 = "ABABAB", str2 = "ABAB"
#Output: "AB"
#
#Example 3:
#
#Input: str1 = "LEET", str2 = "CODE"
#Output: ""
#
# 
#
#Constraints:
#
#    1 <= str1.length, str2.length <= 1000
#    str1 and str2 consist of English uppercase letters.
#


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) < len(str2):
            return Solution._gcd(str1, str2)
        return Solution._gcd(str2, str1)

    @staticmethod
    def _gcd(shortStr, longStr):


        # does the short string have a divisor?
        for n in range(len(shortStr),0,-1):

            if len(shortStr) % n == 0 and len(longStr) % n == 0:
                stimes = len(shortStr) // n
                ltimes = len(longStr) // n
                 
                part = shortStr[0:n] 
                if part * stimes == shortStr and part * ltimes == longStr:
                    return part

        return ""
