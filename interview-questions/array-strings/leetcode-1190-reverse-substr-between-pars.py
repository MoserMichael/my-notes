#1190. Reverse Substrings Between Each Pair of Parentheses
#Medium
#    You are given a string s that consists of lower case English letters and brackets.
#
#    Reverse the strings in each pair of matching parentheses, starting from the innermost one.
#
#    Your result should not contain any brackets.
#
#     
#
#    Example 1:
#
#    Input: s = "(abcd)"
#    Output: "dcba"
#
#    Example 2:
#
#    Input: s = "(u(love)i)"
#    Output: "iloveu"
#    Explanation: The substring "love" is reversed first, then the whole string is reversed.
#
#    Example 3:
#
#    Input: s = "(ed(et(oc))el)"
#    Output: "leetcode"
#    Explanation: First, we reverse the substring "oc", then "etco", and finally, the whole string.
#
#     
#
#    Constraints:
#
#        1 <= s.length <= 2000
#        s only contains lower case English characters and parentheses.
#        It is guaranteed that all parentheses are balanced.
#

class Solution:
    def reverseParentheses(self, s: str) -> str:
        
        pos=[]
        pars=[]

        for idx, ch in enumerate(s):
            if s[idx]=='(':
                pos.append(idx)
            if s[idx]==')':
                entry = (pos.pop(), idx)
                pars.append(entry)

        if len(pars) == 0:
            return s
                
        s = list(s)
        for par in pars:
            s[(par[0]+1):par[1]] = s[(par[0]+1):par[1]][::-1]
                    
        s = filter(lambda cur : cur != "(" and cur != ")", s)
        return "".join(s) 


        ret = s[0:pars[0][0]]+ ret + s[(pars[0][1]+1):]
    
        return ret

