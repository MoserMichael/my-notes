# 187. Repeated DNA Sequences
# Medium
#The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.
#
#    For example, "ACGAATTCCG" is a DNA sequence.
#
#When studying DNA, it is useful to identify repeated sequences within the DNA.
#
#Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in any order.
#
#
#
#Example 1:
#
#Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
#Output: ["AAAAACCCCC","CCCCCAAAAA"]
#
#Example 2:
#
#Input: s = "AAAAAAAAAAAAA"
#Output: ["AAAAAAAAAA"]
#
#
#
#Constraints:
#
#    1 <= s.length <= 105
#    s[i] is either 'A', 'C', 'G', or 'T'.
#



class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:

        low = 0
        high = 10

        dn_count = {}
        ret = []

        while high <= len(s):
            sq = s[low:high]

            prev = dn_count.setdefault(sq, 0)
            dn_count[sq] = prev+1

            if prev == 1:
                ret.append(sq)

            low += 1
            high += 1

        return ret
