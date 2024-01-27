# 227. Basic Calculator II
# Medium
#    Given a string s which represents an expression, evaluate this expression and return its value.
#
#    The integer division should truncate toward zero.
#
#    You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].
#
#    Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().
#
#
#
#    Example 1:
#
#    Input: s = "3+2*2"
#    Output: 7
#
#    Example 2:
#
#    Input: s = " 3/2 "
#    Output: 1
#
#    Example 3:
#
#    Input: s = " 3+5 / 2 "
#    Output: 5
#
#
#
#    Constraints:
#
#        1 <= s.length <= 3 * 105
#        s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
#        s represents a valid expression.
#        All the integers in the expression are non-negative integers in the range [0, 231 - 1].
#        The answer is guaranteed to fit in a 32-bit integer.
#
#


#    # Intuition
#
#    We need to parse an expression of the following form:
#
#    add_expr = mult_expr ( ( "+" | "- ") add_expr ) +
#    mult_expr = number  ( ( "*" | "/ ") mult_expr ) +
#
#    And evaluate that expression while parsing. Luckily no backtracking is needed for this grammar.
#
#    Initially mult_expr was wrong: I can't parse with right-recursion, that does the precedence thing wrong
#
#    It's not 
#    (4 / (2 * 3)) 
#    it's
#    ((4 / 2) * 3)
#

class Solution:
    def calculate(self, s: str) -> int:

        self.tok = re.findall(f'\d+|\+|\-|\*|/', s)
        self.pos = -1

        return self.parse()

    # add_expr = mult_expr ( ( "+" | "- ") add_expr ) +
    def parse(self):
        ret = self.mult_expr()
        
        while (self.pos+1) < len(self.tok):
            op = self.tok[self.pos+1]
            if op == '+' or op =='-':
                self.pos += 1
                arg2 = self.mult_expr()

                #print(f"add: {ret} {op} {arg2}")

                if op == '+':
                    ret += arg2
                elif op == '-':
                    ret -= arg2
            else:
                break

        #print(f"add: {ret}")
        return ret


    # mult_expr = number  ( ( "*" | "/ ") mult_expr ) +
    def mult_expr(self):
        self.pos += 1
        ret = int(self.tok[self.pos])
        
        while (self.pos+1) < len(self.tok):
            
            op = self.tok[self.pos+1]
            if op == '*' or op == '/':
                self.pos += 2
                arg2 = int(self.tok[self.pos])

                #print(f"mult: {ret} {op} {arg2}")

                if op == '*':
                    ret *= arg2
                elif op == '/':
                    ret //= arg2
            else:
                break    

        #print(f"mult: {ret}")
        return ret

        
