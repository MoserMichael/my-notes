# 1657. Determine if Two Strings Are Close
# Medium
#
#    Two strings are considered close if you can attain one from the other using the following operations:
#
#        Operation 1: Swap any two existing characters.
#            For example, abcde -> aecdb
#        Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
#            For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
#
#    You can use the operations on either string as many times as necessary.
#
#    Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.
#
#
#
#    Example 1:
#
#    Input: word1 = "abc", word2 = "bca"
#    Output: true
#    Explanation: You can attain word2 from word1 in 2 operations.
#    Apply Operation 1: "abc" -> "acb"
#    Apply Operation 1: "acb" -> "bca"
#
#    Example 2:
#
#    Input: word1 = "a", word2 = "aa"
#    Output: false
#    Explanation: It is impossible to attain word2 from word1, or vice versa, in any number of operations.
#
#    Example 3:
#
#    Input: word1 = "cabbba", word2 = "abbccc"
#    Output: true
#    Explanation: You can attain word2 from word1 in 3 operations.
#    Apply Operation 1: "cabbba" -> "caabbb"
#    Apply Operation 2: "caabbb" -> "baaccc"
#    Apply Operation 2: "baaccc" -> "abbccc"
#
#
#
#    Constraints:
#
#        1 <= word1.length, word2.length <= 105
#        word1 and word2 contain only lowercase English letters.
#

#    Intuition
#
#    - count all characters in both words, this produces two dictionaries, where the character value is mapped to the number of occurances for that charater.
#    - take the set of keys/characters occuring in the string, if the set of keys is different for both strings, then the answer is False
#    - take the set of values of both maps/the number of occuranes of each character in a string, sort them. If the result is different, then swapping will not fix the strings.
#


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:

        chmap1 = Solution.countChars(word1)
        chmap2 = Solution.countChars(word2)

        cnt1=list(chmap1.values())
        cnt2=list(chmap2.values())
        cnt1.sort()
        cnt2.sort()
        if cnt1 != cnt2:
            return False

        if set(chmap1.keys()) != set(chmap2.keys()):
            return False
        return True

    def countChars(word):
        ret={}
        for ch in word:
            ret[ch]=ret.setdefault(ch, 0) + 1
        return ret

