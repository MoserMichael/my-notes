# 97. Interleaving String
# Medium
#
#    Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.
#
#    An interleaving of two strings s and t is a configuration where s and t are divided into n and m
#    substrings
#    respectively, such that:
#
#        s = s1 + s2 + ... + sn
#        t = t1 + t2 + ... + tm
#        |n - m| <= 1
#        The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
#
#    Note: a + b is the concatenation of strings a and b.
#
#
#
#    Example 1:
#
#    Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
#    Output: true
#    Explanation: One way to obtain s3 is:
#    Split s1 into s1 = "aa" + "bc" + "c", and s2 into s2 = "dbbc" + "a".
#    Interleaving the two splits, we get "aa" + "dbbc" + "bc" + "a" + "c" = "aadbbcbcac".
#    Since s3 can be obtained by interleaving s1 and s2, we return true.
#
#    Example 2:
#
#    Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
#    Output: false
#    Explanation: Notice how it is impossible to interleave s2 with any other string to obtain s3.
#
#    Example 3:
#
#    Input: s1 = "", s2 = "", s3 = ""
#    Output: true
#
#
#
#    Constraints:
#
#        0 <= s1.length, s2.length <= 100
#        0 <= s3.length <= 200
#        s1, s2, and s3 consist of lowercase English letters.
#
#
#
#    Follow up: Could you solve it using only O(s2.length) additional memory space?
#


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        if len(s3) != len(s1) + len(s2):
            return False

        if not Solution.excludeByCount(s1, s2, s3):
            return False

        return Solution.dp(s1, 0, s2, 0, s3, 0, set())


    def excludeByCount(s1, s2, s3):
        count = {}

        for ch in s1:
            count[ch] = count.setdefault(ch, 0) + 1

        for ch in s2:
            count[ch] = count.setdefault(ch, 0) + 1

        for ch in s3:
            count[ch] = count.setdefault(ch, 0) - 1

        for cnt in count.values():
            if cnt != 0:
                return False

        return True


    def dp(s1, s1_idx, s2, s2_idx, s3, s3_idx, memo):

        key = f"{s1_idx}-{s2_idx}"
        if key in memo:
            return False

        if s3_idx == len(s3):
            if s1_idx == len(s1) and s2_idx == len(s2):
                return True
        elif s1_idx < len(s1) and s2_idx < len(s2) and s1[s1_idx] == s2[s2_idx] == s3[s3_idx]:
            if Solution.dp(s1, s1_idx+1, s2, s2_idx, s3, s3_idx+1, memo):
                return True
            if Solution.dp(s1, s1_idx, s2, s2_idx+1, s3, s3_idx+1, memo):
                return True

        elif s1_idx < len(s1) and s1[s1_idx] == s3[s3_idx]:

            if Solution.dp(s1, s1_idx+1, s2, s2_idx, s3, s3_idx+1, memo):
                return True

        elif s2_idx < len(s2) and s2[s2_idx] == s3[s3_idx]:

            if Solution.dp(s1, s1_idx, s2, s2_idx+1, s3, s3_idx+1, memo):
                return True

        memo.add(key)
        return False

