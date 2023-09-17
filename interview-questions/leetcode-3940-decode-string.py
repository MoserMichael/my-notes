# 394. Decode String
# Medium
#
#Given an encoded string, return its decoded string.
#
#The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.
#
#You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].
#
#The test cases are generated so that the length of the output will never exceed 105.
#
# 
#
#Example 1:
#
#Input: s = "3[a]2[bc]"
#Output: "aaabcbc"
#
#Example 2:
#
#Input: s = "3[a2[c]]"
#Output: "accaccacc"
#
#Example 3:
#
#Input: s = "2[abc]3[cd]ef"
#Output: "abcabccdcdcdef"
#
# 
#
#Constraints:
#
#    1 <= s.length <= 30
#    s consists of lowercase English letters, digits, and square brackets '[]'.
#    s is guaranteed to be a valid input.
#    All the integers in s are in the range [1, 300].
#
#

class Solution:
    def decodeString(self, s: str) -> str:
        res, pos = self.parseString(s, 0)
        assert pos == len(s)
        return res


    # s = simple +
    #
    # simple = ( <digit>+ [ s ] ) +
    # simple = <asciletters>+

    def parseString(self, s, pos):
        res = ""

        while pos < len(s):
            ch = s[pos]
            if ch.isdigit():
                resNow, pos = self.parseRep(s, pos)
            elif ch.isalpha():
                resNow, pos = self.parseTok(s, pos)
            res += resNow

            if pos < len(s) and s[pos]==']':
                break           

        return res, pos
        
    def parseRep(self, s, pos):
        cur = pos
        while cur < len(s) and s[cur].isdigit():
            cur += 1
        nrep = int(s[pos:cur])

        if s[cur] == '[':
            cur += 1
        else:
            raise Exception(f"expected [ at {cur}")

        rep, cur = self.parseString(s, cur)

        if s[cur] == ']':
            cur += 1
        else:
            raise Exception(f"expected ] at {cur}")

        return rep * nrep, cur

    def parseTok(self, s, pos):
        cur = pos
        while cur < len(s) and s[cur].isalpha():
            cur += 1
        return s[pos:cur], cur

