# 14. Longest Common Prefix
# Easy
#Write a function to find the longest common prefix string amongst an array of strings.
#
#If there is no common prefix, return an empty string "".
#
#
#
#Example 1:
#
#Input: strs = ["flower","flow","flight"]
#Output: "fl"
#
#Example 2:
#
#Input: strs = ["dog","racecar","car"]
#Output: ""
#Explanation: There is no common prefix among the input strings.
#
#
#
#Constraints:
#
#    1 <= strs.length <= 200
#    0 <= strs[i].length <= 200
#    strs[i] consists of only lowercase English letters.
#



class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not len(strs):
            return 0
        pset = set()

        first_word = strs[0]
        for idx in range(1, len(first_word)+1):
            pset.add(first_word[0:idx])
        longest_prefix=len(first_word)

        for cur_word in strs[1:]:

            cur_longest_prefix = 0
            for word_idx in range(1, min(longest_prefix, len(cur_word))+1):
                subs = cur_word[0:word_idx]
                if subs not in pset:
                    break
                cur_longest_prefix = word_idx

            longest_prefix = cur_longest_prefix
            if longest_prefix == 0:
                break

        return first_word[0:longest_prefix]


