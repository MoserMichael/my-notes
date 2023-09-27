class Solution:
    def reverseWords(self, s: str) -> str:
        reversedWordList = s.split()
        
        reversedWordList.reverse()

        return " ".join(reversedWordList)
        
