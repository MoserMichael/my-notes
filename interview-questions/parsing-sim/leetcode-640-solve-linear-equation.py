# 640. Solve the Equation
# Medium
#    Solve a given equation and return the value of 'x' in the form of a string "x=#value". The equation contains only '+', '-' operation, the variable 'x' and its coefficient. You should return "No solution" if there is no solution for the equation, or "Infinite solutions" if there are infinite solutions for the equation.
#
#    If there is exactly one solution for the equation, we ensure that the value of 'x' is an integer.
#
#     
#
#    Example 1:
#
#    Input: equation = "x+5-3+x=6+x-2"
#    Output: "x=2"
#
#    Example 2:
#
#    Input: equation = "x=x"
#    Output: "Infinite solutions"
#
#    Example 3:
#
#    Input: equation = "2x=x"
#    Output: "x=0"
#
#     
#
#    Constraints:
#
#        3 <= equation.length <= 1000
#        equation has exactly one '='.
#        equation consists of integers with an absolute value in the range [0, 100] without any leading zeros, and the variable 'x'.
#

import re

class Solution:
    def solveEquation(self, equation: str) -> str:
        tokens = re.findall(r'x|\+|\-|=|\d+', equation)

        sign = 1
        factor = 1

        x_count = 0 
        const_count = 0       

        idx = 0
        while idx < len(tokens):
            if tokens[idx] == '+':
                sign = 1
            elif tokens[idx] == '-':
                sign = -1
            elif tokens[idx] == '=':
                factor = -1
                sign = 1
            elif tokens[idx] == 'x':
                x_count += factor * sign
            else:
                # number
                if idx + 1 < len(tokens) and tokens[idx+1] == 'x':
                    x_count += int(tokens[idx]) * factor * sign
                    idx += 1
                else:
                    const_count += int(tokens[idx]) * -factor * sign

            idx += 1


        if x_count == 0:
            if const_count == 0:
                return "Infinite solutions"
            return "No solution" 
        
        return f"x={int(const_count / x_count)}"
