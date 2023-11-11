# 91. Decode Ways
# Medium
#    A message containing letters from A-Z can be encoded into numbers using the following mapping:
#
#    'A' -> "1"
#    'B' -> "2"
#    ...
#    'Z' -> "26"
#
#    To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:
#
#        "AAJF" with the grouping (1 1 10 6)
#        "KJF" with the grouping (11 10 6)
#
#    Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".
#
#    Given a string s containing only digits, return the number of ways to decode it.
#
#    The test cases are generated so that the answer fits in a 32-bit integer.
#
#
#
#    Example 1:
#
#    Input: s = "12"
#    Output: 2
#    Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).
#
#    Example 2:
#
#    Input: s = "226"
#    Output: 3
#    Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
#
#    Example 3:
#
#    Input: s = "06"
#    Output: 0
#    Explanation: "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06").
#
#
#
#    Constraints:
#
#        1 <= s.length <= 100
#        s contains only digits and may contain leading zero(s).
#

class Solution:
    def numDecodings(self, s: str) -> int:
        return Solution.norec(s)
        #return Solution.recWithMemo(s)

    def norec(s):
        val = [0] * len(s)
        for idx in range(len(s)-1, -1, -1):
            if s[idx] == "0":
                val[idx] = 0
                continue

            n_at = val[idx+1] if idx < (len(s)-1) else 1

            n_at_two = 0
            at_two = s[idx : (idx+2)]

            if len(at_two)==2 and 1 <= int(at_two) <= 26:
                n_at_two = val[idx+2] if (idx+2) < len(s) else 1

            val[idx] = n_at + n_at_two

        return val[0]


    def recWithMemo(s):
        memo={}
        return Solution.rec(s, 0, memo)



    def rec(s, pos, memo):
        if pos >= len(s):
            return pos == len(s)

        if pos in memo:
            return memo[pos]

        at = s[pos:(pos+1)]
        at_two = s[pos:(pos+2)]

        n_at = Solution.rec(s, pos+1, memo) if int(at) > 0 else 0
        n_at_two = 0

        if at_two != at:
            n_val = int(at_two)
            if 1 <= n_val <= 26 and at_two[0] != '0':
                n_at_two = Solution.rec(s, pos+2, memo)

        r = n_at + n_at_two
        memo[pos] = r

        return r

