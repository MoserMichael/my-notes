# 678. Valid Parenthesis String
# Medium
#
#    Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.
#
#    The following rules define a valid string:
#
#        Any left parenthesis '(' must have a corresponding right parenthesis ')'.
#        Any right parenthesis ')' must have a corresponding left parenthesis '('.
#        Left parenthesis '(' must go before the corresponding right parenthesis ')'.
#        '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".
#
#
#
#    Example 1:
#
#    Input: s = "()"
#    Output: true
#
#    Example 2:
#
#    Input: s = "(*)"
#    Output: true
#
#    Example 3:
#
#    Input: s = "(*))"
#    Output: true
#
#
#
#    Constraints:
#
#        1 <= s.length <= 100
#        s[i] is '(', ')' or '*'.
#
#


#    # Intuition
#
#    # Code
#
#    maintain a stack of still open parenthesis (record the position of each parenthesis) and a stack of stars (record the position of each star)
#
#    - for a ( in the input: push the position of the character to the parenthesis stack
#    - for a * in the input: push the position of the character to the stars stack
#    - for a ) in the input:
#        - if the parenthesis stack is not empty: pop an element (the parenthesis has a preceeding parenthesis)
#        - else if the stars stack is not empty: pop an element (the star counts as a peceeding parenthesis)
#        - if both are empty: the string is not well formed
#
#    for the remaining parenthesis: check that we have a star that comes after the parenthesis - that's why you need to maintain the position of each symbol!
#
#    if you have more parenthesis than stars then the string is not well formed - the stars can't be used to close the parenthesis.
#
#    otherwise check that each parenthesis has a star that comes after it (working from the end is faster, you don't need to remove an element from the middle)
#

class Solution:
    def checkValidString(self, s: str) -> bool:
        stars = []
        parenthesis = []

        for idx, ch in enumerate(s):
            if ch == '(':
                parenthesis.append(idx)
            elif ch == '*':
                stars.append(idx)
            elif ch == ')':
                if parenthesis:
                    parenthesis.pop()
                elif stars:
                    stars.pop()
                else:
                    return False

        if len(parenthesis) > len(stars):
            return False

        # problem: fo the remaining parenthesis: check that we have a star that comes after the parenthesis
        # that's why you need to maintain the position of each symbol

        # works, but slowly
        #for idx_p in parenthesis:
        #    valid = False
        #    for idx, idx_s in enumerate(stars):
        #        if idx_s > idx_p:
        #            del stars[idx]
        #            valid = True
        #            break
        #    if not valid:
        #        return False

        # work from the end - much easier
        while parenthesis:
            p_pos = parenthesis.pop()
            s_pos = stars.pop()
            if s_pos < p_pos:
                return False

        return True

