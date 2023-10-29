# 115. Distinct Subsequences
# Hard
#    Given two strings s and t, return the number of distinct subsequences of s which equals t.
#
#    The test cases are generated so that the answer fits on a 32-bit signed integer.
#
#
#
#    Example 1:
#
#    Input: s = "rabbbit", t = "rabbit"
#    Output: 3
#    Explanation:
#    As shown below, there are 3 ways you can generate "rabbit" from s.
#    rabbbit
#    rabbbit
#    rabbbit
#
#    Example 2:
#
#    Input: s = "babgbag", t = "bag"
#    Output: 5
#    Explanation:
#    As shown below, there are 5 ways you can generate "bag" from s.
#    babgbag
#    babgbag
#    babgbag
#    babgbag
#    babgbag
#
#
#
#    Constraints:
#
#        1 <= s.length, t.length <= 1000
#        s and t consist of English letters.
#

class Solution:

    def numDistinct(self, s: str, t: str) -> int:
        
        if len(s) == len(t):
            return 1 if s == t else 0

        row=[-1] * len(t)
        memo = [row.copy() for i in range(0,len(s)) ]
        return Solution.rec(s, 0, t, 0, memo)

    def rec(s, s_idx, t, t_idx, memo):
        if t_idx == len(t):
            return 1
        if s_idx == len(s):
            return 0
        
        v = memo[s_idx][t_idx]
        if v != -1:
            return v

        sum = Solution.rec(s, s_idx+1, t, t_idx, memo)     

        if s[s_idx] == t[t_idx]:
           sum += Solution.rec(s, s_idx+1, t, t_idx+1, memo)      
        memo[s_idx][t_idx] = sum
        return sum

