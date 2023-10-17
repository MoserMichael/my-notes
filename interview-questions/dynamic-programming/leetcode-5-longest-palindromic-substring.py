# 5. Longest Palindromic Substring
# Medium
#Given a string s, return the longest
#palindromic
#substring
#in s.
#
#
#
#Example 1:
#
#Input: s = "babad"
#Output: "bab"
#Explanation: "aba" is also a valid answer.
#
#Example 2:
#
#Input: s = "cbbd"
#Output: "bb"
#
#
#
#Constraints:
#
#    1 <= s.length <= 1000
#    s consist of only digits and English letters.
#

class Solution:
    def longestPalindrome(self, s: str) -> str:

        if not len(s):
            return ""

        ret_palindrom = s[-1]
        ret_palindrom_len = 1

        palindrom_set = set()

        for slen in range(2, len(s)+1):
            
            if slen - 2 > 0 and ret_palindrom_len < (slen-2):
                return ret_palindrom

            for pos in range(0, len(s)-slen+1):
                to_check = s[pos : (pos + slen)]
                rs = Solution.is_palindrom(to_check, palindrom_set)
                if rs:
                    if slen > ret_palindrom_len:
                        ret_palindrom_len = slen
                        ret_palindrom = to_check

        return ret_palindrom

    def is_palindrom(to_check, palindrom_set):

        if to_check in palindrom_set:
            return True

        ln = len(to_check)
        if ln <= 1:
            return True
    
        if to_check[0] != to_check[-1]:
            return False
        rt = Solution.is_palindrom(to_check[1:(len(to_check)-1)], palindrom_set)
        if rt:            
            palindrom_set.add(to_check)

        return rt
