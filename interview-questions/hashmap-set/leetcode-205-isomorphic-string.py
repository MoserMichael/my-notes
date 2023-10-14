# 205. Isomorphic Strings
# Easy
#Given two strings s and t, determine if they are isomorphic.
#
#Two strings s and t are isomorphic if the characters in s can be replaced to get t.
#
#All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.
#
#
#
#Example 1:
#
#Input: s = "egg", t = "add"
#Output: true
#
#Example 2:
#
#Input: s = "foo", t = "bar"
#Output: false
#
#Example 3:
#
#Input: s = "paper", t = "title"
#Output: true
#
#
#
#Constraints:
#
#    1 <= s.length <= 5 * 104
#    t.length == s.length
#    s and t consist of any valid ascii character.

import re

class Solution:

    def isIsomorphic(self, s: str, t: str) -> bool:

        #return Solution.isIsomorphicSlow(s, t)
        return Solution.isIsomorphicFaster(s, t)

    def isIsomorphicFaster(s, t):
        if len(s) != len(t):
            return False

        s_map, s_pos = Solution.countCharsWithPos(s)
        t_map = Solution.countChars(t)

        if len(s_map) != len(t_map):
            return False

        return Solution.trySubstituteFast(s, t, s_pos)

    def trySubstituteFast(s, t, s_pos):
        stmp = list(s)
        substituted_idx = set()

        for idx in range(0, len(s)):
            if idx not in substituted_idx and s[idx] != t[idx]:
                for idx2 in s_pos[ s[idx] ]:
                    stmp[idx2] = t[idx]
                    substituted_idx.add(idx2)

        stmp = "".join(stmp)
        return stmp == t

    def countCharsWithPos(s):
        countMap = {}
        charPosMap = {}

        for idx in range(0, len(s)):
            ch = s[idx]
            countMap[ch] = countMap.setdefault(ch, 0) + 1

            val = charPosMap.setdefault(ch, [])
            val.append(idx)
            charPosMap[ch] = val

        return countMap, charPosMap


    def isIsomorphicSlow(s, t):
        if len(s) != len(t):
            return False

        s_map = Solution.countChars(s)
        t_map = Solution.countChars(t)
        if len(s_map) != len(t_map):
            return False

        #if set(s_map.values()) != set(t_map.values()):
        #    return False

        return Solution.trySubstitute(s, t)

    def trySubstitute(s, t):
        stmp = list(s)
        substituted_idx = set()

        for idx in range(0, len(s)):
            if idx not in substituted_idx and s[idx] != t[idx] :
                for idx2 in range(0, len(s)):
                    if s[idx2] == s[idx]:
                        stmp[idx2] = t[idx]
                        substituted_idx.add(idx2)

        stmp = "".join(stmp)
        return stmp == t


    def countChars(s):
        countMap = {}
        for ch in s:
            countMap[ch] = countMap.setdefault(ch, 0) + 1

        return countMap
