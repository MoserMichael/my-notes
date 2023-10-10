# 383. Ransom Note
# Easy
#Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
#
#Each letter in magazine can only be used once in ransomNote.
#
#
#
#Example 1:
#
#Input: ransomNote = "a", magazine = "b"
#Output: false
#
#Example 2:
#
#Input: ransomNote = "aa", magazine = "ab"
#Output: false
#
#Example 3:
#
#Input: ransomNote = "aa", magazine = "aab"
#Output: true
#
#
#
#Constraints:
#
#    1 <= ransomNote.length, magazine.length <= 105
#    ransomNote and magazine consist of lowercase English letters.
#

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        cmap = Solution.countMap(magazine)

        for ch in ransomNote:
            if ch not in cmap:
                return False
            cmap[ch] -= 1
            if cmap[ch] < 0:
                return False
        
        return True

    def countMap(big_str):
        word_freq = {}

        for ch in big_str:
            word_freq[ ch ] = word_freq.setdefault( ch, 0) + 1

        return word_freq



        
