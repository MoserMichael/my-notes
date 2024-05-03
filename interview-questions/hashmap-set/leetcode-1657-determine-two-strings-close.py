# 1657. Determine if Two Strings Are Close
# Medium
#Two strings are considered close if you can attain one from the other using the following operations:
#
#    Operation 1: Swap any two existing characters.
#        For example, abcde -> aecdb
#    Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
#        For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
#
#You can use the operations on either string as many times as necessary.
#
#Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.
#
#
#
#Example 1:
#
#Input: word1 = "abc", word2 = "bca"
#Output: true
#Explanation: You can attain word2 from word1 in 2 operations.
#Apply Operation 1: "abc" -> "acb"
#Apply Operation 1: "acb" -> "bca"
#
#Example 2:
#
#Input: word1 = "a", word2 = "aa"
#Output: false
#Explanation: It is impossible to attain word2 from word1, or vice versa, in any number of operations.
#
#Example 3:
#
#Input: word1 = "cabbba", word2 = "abbccc"
#Output: true
#Explanation: You can attain word2 from word1 in 3 operations.
#Apply Operation 1: "cabbba" -> "caabbb"
#Apply Operation 2: "caabbb" -> "baaccc"
#Apply Operation 2: "baaccc" -> "abbccc"
#
#
#
#Constraints:
#
#    1 <= word1.length, word2.length <= 105
#    word1 and word2 contain only lowercase English letters.
#


import collections

import collections

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:

        if len(word1) != len(word2):
            return False

        cnt1, keys1 = Solution.countChars(word1)
        cnt2, keys2 = Solution.countChars(word2)

        return cnt1 == cnt2 and keys1 == keys2

    def countChars(word):
        ret = collections.Counter(word)

        #ret = collections.defaultdict(int)
        #for ch in word:
        #    ret[ch] += 1

        #ret={}
        #for ch in word:
        #    ret[ch]=ret.setdefault(ch, 0) + 1

        cret = list(ret.values())
        cret.sort()
        return cret, set(ret.keys())


#class Solution:
#    def closeStrings(self, word1: str, word2: str) -> bool:
#        if len(word1) != len(word2):
#            return False
#
#        freq1, vals1 = self.countFreq(word1)
#        freq2, vals2 = self.countFreq(word2)
#
#        return freq1 == freq2 and vals1 == vals2
#
#
#    def countFreq(self, word):
#        freq = {}
#        for ch in word:
#            if ch in freq:
#                freq[ch] += 1
#            else:
#                freq[ch] = 1
#
#        vals = list(freq.values())
#        vals.sort()
#
#        keys = list(freq.keys())
#        keys.sort()
#
#        return vals, keys
#

