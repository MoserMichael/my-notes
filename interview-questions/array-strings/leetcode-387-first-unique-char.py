# 387. First Unique Character in a String
# Easy
#
#    Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
#
#
#
#    Example 1:
#
#    Input: s = "leetcode"
#    Output: 0
#
#    Example 2:
#
#    Input: s = "loveleetcode"
#    Output: 2
#
#    Example 3:
#
#    Input: s = "aabb"
#    Output: -1
#
#
#
#    Constraints:
#
#        1 <= s.length <= 105
#        s consists of only lowercase English letters.
#
#


class Entry:
    def __init__(self, first_pos):
        self.first_pos = first_pos
        self.count = 1

class Solution:
    def firstUniqChar(self, s: str) -> int:
        map_char = {}

        for idx in range(0, len(s)):
            ch = s[idx]
            if ch not in map_char:
                map_char[ ch ] = Entry(idx)
            else:
                map_char[ ch ].count += 1

        min_pos = -1
        for val in map_char.values():
            if val.count == 1:
                if min_pos == -1:
                    min_pos = val.first_pos
                else:
                    min_pos = min(min_pos, val.first_pos)

        return min_pos
