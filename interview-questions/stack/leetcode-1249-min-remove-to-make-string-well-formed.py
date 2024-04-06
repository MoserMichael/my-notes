# 1249. Minimum Remove to Make Valid Parentheses
# Medium
#
#    Given a string s of '(' , ')' and lowercase English characters.
#
#    Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.
#
#    Formally, a parentheses string is valid if and only if:
#
#        It is the empty string, contains only lowercase characters, or
#        It can be written as AB (A concatenated with B), where A and B are valid strings, or
#        It can be written as (A), where A is a valid string.
#
#
#
#    Example 1:
#
#    Input: s = "lee(t(c)o)de)"
#    Output: "lee(t(c)o)de"
#    Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
#
#    Example 2:
#
#    Input: s = "a)b(c)d"
#    Output: "ab(c)d"
#
#    Example 3:
#
#    Input: s = "))(("
#    Output: ""
#    Explanation: An empty string is also valid.
#
#
#
#    Constraints:
#
#        1 <= s.length <= 105
#        s[i] is either'(' , ')', or lowercase English letter.
#


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stk = []
        remove_idx = []

        for idx, ch in enumerate(list(s)):
            if ch == '(':
                stk.append( idx )
            elif ch == ')':
                if len(stk) > 0:
                    stk.pop()
                else:
                    remove_idx.append(idx)

        remove_idx = remove_idx + stk


        #print(remove_idx)

        ret = s
        for idx in remove_idx[::-1]:
            ret = ret[0:idx] + ret[(idx+1):]
            #print(idx, ret)

        return ret
