# 345. Reverse Vowels of a String
#
#Given a string s, reverse only all the vowels in the string and return it.
#
#The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
#
#Example 1:
#
#Input: s = "hello"
#Output: "holle"
#
#Example 2:
#
#Input: s = "leetcode"
#Output: "leotcede"
#
 

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels={'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

        vowelPos = []
        for pos, ch in enumerate(s):
            if ch in vowels:
                vowelPos.append( (ch, pos) )


        strLst = list(s)

        for idx in range(0, len(vowelPos)):
            reverseIdx = len(vowelPos) - idx - 1

            entry = vowelPos[idx]
            reverseEntry = vowelPos[reverseIdx]

            #print(f"idx: {reverseEntry[1]} ch: {entry[0]}")

            strLst[ reverseEntry[1] ] = entry[0] 
            
        return ''.join(strLst)
