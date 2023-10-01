# 3. Longest Substring Without Repeating Characters
# Medium
#Given a string s, find the length of the longest
#substring
#without repeating characters.
#
#
#
#Example 1:
#
#Input: s = "abcabcbb"
#Output: 3
#Explanation: The answer is "abc", with the length of 3.
#
#Example 2:
#
#Input: s = "bbbbb"
#Output: 1
#Explanation: The answer is "b", with the length of 1.
#
#Example 3:
#
#Input: s = "pwwkew"
#Output: 3
#Explanation: The answer is "wke", with the length of 3.
#Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
#
#
#
#Constraints:
#
#    0 <= s.length <= 5 * 104
#    s consists of English letters, digits, symbols and spaces.
#




class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        left = 0
        right = 0
        max_len = 0
        
        char_map = {}
        repeat_chars = 0

        while left < len(s):

            if repeat_chars:
                assert left != right

            if right < len(s) and not repeat_chars:
                right += 1
                
                ch = s[right-1]

                if ch in char_map: 
                    char_map[ch] += 1
                    repeat_chars += 1
                else:
                    char_map[ch] = 1

                #print(f"+ {left}..{right} s {s[left:right]} repeat {repeat_chars} {char_map}")
                if not repeat_chars and max_len < (right - left):
                    max_len = right - left
                    #print(f"max: {left} {right} - {max_len}")

            
            if repeat_chars:                    
                if left < right:
                    ch = s[left]
                    if ch in char_map:
                        char_map[ch] -= 1
                        if char_map[ch] == 0:
                            char_map.pop(ch)
                        else:
                            repeat_chars -= 1

                    else:
                        assert False
                    
                    left += 1                                        
                    #print(f"- {left}..{right} s: {s[left:right]} repeat {repeat_chars} {char_map}")

                    if not repeat_chars and max_len < (right - left):
                        max_len = right - left + 1
                        #print(f"max: {left} {right}  - {max_len}")

            else:
                if right == len(s):
                    break

        if max_len == math.inf:
            return 0
        return max_len
