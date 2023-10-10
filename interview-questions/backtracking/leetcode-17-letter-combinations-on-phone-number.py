# 17. Letter Combinations of a Phone Number
# Medium
#Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
#
#A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
#
#
#
#Example 1:
#
#Input: digits = "23"
#Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
#
#Example 2:
#
#Input: digits = ""
#Output: []
#
#Example 3:
#
#Input: digits = "2"
#Output: ["a","b","c"]
#
#
#
#Constraints:
#
#    0 <= digits.length <= 4
#    digits[i] is a digit in the range ['2', '9'].
#

class Solution:
    keyboard = {
"2": "abc",
"3": "def",
"4": "ghi",
"5": "jkl",
"6": "mno",
"7": "pqrs",
"8": "tuv",
"9": "wxyz"
}

    def letterCombinations(self, digits: str) -> List[str]:
        ret = []
        if len(digits) != 0:
            Solution.combine(digits, 0, ret, [])
        return ret

    def combine(digit_str, pos, ret, stack):
            if pos >= len(digit_str):
                ret.append( "".join(stack) )
                return

            cur_digit = digit_str[pos]

            for ch in Solution.keyboard[ cur_digit ]:
                stack.append(ch)
                Solution.combine(digit_str, pos+1, ret, stack)
                stack.pop()





