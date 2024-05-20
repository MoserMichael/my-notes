# 2405. Optimal Partition of String
# Medium
#
#    Given a string s, partition the string into one or more substrings such that the characters in each substring are unique. That is, no letter appears in a single substring more than once.
#
#    Return the minimum number of substrings in such a partition.
#
#    Note that each character should belong to exactly one substring in a partition.
#
#
#
#    Example 1:
#
#    Input: s = "abacaba"
#    Output: 4
#    Explanation:
#    Two possible partitions are ("a","ba","cab","a") and ("ab","a","ca","ba").
#    It can be shown that 4 is the minimum number of substrings needed.
#
#    Example 2:
#
#    Input: s = "ssssss"
#    Output: 6
#    Explanation:
#    The only valid partition is ("s","s","s","s","s","s").
#
#
#
#    Constraints:
#
#        1 <= s.length <= 105
#        s consists of only English lowercase letters.
#
#

class Solution:
    def partitionString(self, s: str) -> int:
        if s == "":
            return 0
        return Solution.withStr(s)
        #return Solution.withSet(s)

    # why is it that using strings instead of sets appears to be faster?
    # probably depends on the length of the string.
    # would probably be different if they had longer strings ...

    def withStr(s):
        mem = ""
        ret = 1
        for ch in s:
            if ch in mem:
                ret += 1
                #mem.clear()
                mem = ""
            mem += ch

        return ret


    def withSet(s):
        mem = set()
        ret = 1
        for ch in s:
            if ch in mem:
                ret += 1
                mem.clear()
            mem.add(ch)

        return ret


