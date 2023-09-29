# 20. Valid Parentheses
# Easy
#Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
#An input string is valid if:
#
#    Open brackets must be closed by the same type of brackets.
#    Open brackets must be closed in the correct order.
#    Every close bracket has a corresponding open bracket of the same type.
#
#
#
#Example 1:
#
#Input: s = "()"
#Output: true
#
#Example 2:
#
#Input: s = "()[]{}"
#Output: true
#
#Example 3:
#
#Input: s = "(]"
#Output: false
#
#
#
#Constraints:
#
#    1 <= s.length <= 104
#    s consists of parentheses only '()[]{}'.
#



class Solution:

    def isValid(self, s: str) -> bool:

        stack = []
        for par in s:
            if Solution.isOpeningPar(par):
                stack.append(par)
            else:
                if len(stack) == 0:
                    return False
                ch = stack.pop()
                if not Solution.isMatching(ch, par):
                    return False

        return len(stack) == 0


    @staticmethod
    def isMatching(op, cl):
        if cl == '}':
            return op == '{'
        if cl == ')':
            return op == '('
        if cl == ']':
            return op == '['
        return False

    @staticmethod
    def isOpeningPar(ch):
        return ch=='{' or ch == '(' or ch == '['
