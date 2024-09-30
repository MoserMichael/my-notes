# 214. Shortest Palindrome
# Hard
#
#    You are given a string s. You can convert s to a
#    palindrome
#    by adding characters in front of it.
#
#    Return the shortest palindrome you can find by performing this transformation.
#
#     
#
#    Example 1:
#
#    Input: s = "aacecaaa"
#    Output: "aaacecaaa"
#
#    Example 2:
#
#    Input: s = "abcd"
#    Output: "dcbabcd"
#
#     
#
#    Constraints:
#
#        0 <= s.length <= 5 * 104
#        s consists of lowercase English letters only.
#


class Solution:
    def shortestPalindrome(self, s: str) -> str:

        if s == "":
            return ""

        for idx in range(len(s)-1, -1, -1):
            idx2 = idx
            while idx2 != -1:
                if s[idx2] != s[idx-idx2]:
                    break
                idx2 -= 1
            if idx2 == -1:
                return s[(idx+1):][::-1] + s

