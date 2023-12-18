# 438. Find All Anagrams in a String
# Medium
#    Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.
#
#    An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
#
#
#
#    Example 1:
#
#    Input: s = "cbaebabacd", p = "abc"
#    Output: [0,6]
#    Explanation:
#    The substring with start index = 0 is "cba", which is an anagram of "abc".
#    The substring with start index = 6 is "bac", which is an anagram of "abc".
#
#    Example 2:
#
#    Input: s = "abab", p = "ab"
#    Output: [0,1,2]
#    Explanation:
#    The substring with start index = 0 is "ab", which is an anagram of "ab".
#    The substring with start index = 1 is "ba", which is an anagram of "ab".
#    The substring with start index = 2 is "ab", which is an anagram of "ab".
#
#
#
#    Constraints:
#
#        1 <= s.length, p.length <= 3 * 104
#        s and p consist of lowercase English letters.
#


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []


        init_map = Solution.countChar(p)

        # in the sliding window: maintain the map that counts the characters in the anagra,
        cur_map = init_map.copy()
        low=high=0

        ret = []

        while high<len(s):
            ch=s[high]
            if ch in cur_map:

                # if character occrus in anagram, widen window and decrement the count
                cur_map[ch] -= 1
                high += 1

                # if number of characters dropped to zer - remove map entry
                if cur_map[ch] == 0:
                    cur_map.pop(ch)

                    # if map is empty - we have a match
                    if len(cur_map) == 0:
                        ret.append(low)

                        cur_map[ s[low] ] = 1
                        low = low+1


            else:
                # that's the tricky part!!!

                if ch in init_map:
                    if s[low] == ch:
                        cur_map[s[low]] = 1
                        low += 1
                    else:
                        cur_map[s[low]] = cur_map.setdefault(s[low], 0) + 1
                        low += 1
                        #low = high = low+1
                        #cur_map = init_map.copy()
                else:
                    # if next char not part of anagram - start from scratch (after that position)
                    low = high = high+1
                    cur_map = init_map.copy()

                #if ch in init_map:
                #    low = high = low+1
                #else:
                #    low = high = high+1
                #cur_map = init_map.copy()

        return ret


    def countChar(p):
        m = {}
        for ch in p:
            m[ch] = m.setdefault(ch, 0) + 1

        return m


