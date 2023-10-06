# 224. Basic Calculator
# Hard
#Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.
#
#Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().
#
#
#
#Example 1:
#
#Input: s = "1 + 1"
#Output: 2
#
#Example 2:
#
#Input: s = " 2-1 + 2 "
#Output: 3
#
#Example 3:
#
#Input: s = "(1+(4+5+2)-3)+(6+8)"
#Output: 23
#
#
#
#Constraints:
#
#    1 <= s.length <= 3 * 105
#    s consists of digits, '+', '-', '(', ')', and ' '.
#    s represents a valid expression.
#    '+' is not used as a unary operation (i.e., "+1" and "+(2 + 3)" is invalid).
#    '-' could be used as a unary operation (i.e., "-1" and "-(2 + 3)" is valid).
#    There will be no two consecutive operators in the input.
#    Every number and running calculation will fit in a signed 32-bit integer.
#

import re
import math

class Solution:
    TOKEN_BR_OPEN = 1
    TOKEN_BR_CLOSE = 2
    TOKEN_OP = 3
    TOKEN_UINT = 4

    def calculate(self, s: str) -> int:
        #print(f"expr: {s}")
        toks = Solution.tokenize(s)
        #print(f"tokens: {toks}")
        idx, ret_val =  Solution.parse_expr(toks, 0)
        if idx < len(toks)-1:
            raise Exception(f"not all expression parsed {idx} .. {len(toks)}")
        return ret_val


    @staticmethod
    def parse_expr(toks, idx):
        ret_val = 0

        if idx == len(toks):
            return idx, ret_val

        idx_start = idx
        start_tok = toks[idx]

        idx, ret_val = Solution.parse_simple(toks, idx)

        while idx < len(toks):
            op = toks[idx]
            if op[0] != Solution.TOKEN_OP:
                return idx, ret_val

            idx += 1
            idx, arg_two = Solution.parse_simple(toks, idx)

            if op[1] == '+':
                ret_val += arg_two
            elif op[1] == '-':
                ret_val -= arg_two
            else:
                raise Exception(f"Illegal operator {op}")

        #print(f"->expr {idx_start} .. {idx} = {ret_val}- {start_tok}")
        return idx, ret_val

    @staticmethod
    def parse_simple(toks, idx):

        if idx == len(toks):
            return -1, 0

        idx_start = idx
        start_tok = toks[idx]

        if start_tok[0] == Solution.TOKEN_UINT:
            ret_val = start_tok[1]
            idx += 1
        elif start_tok[0] == Solution.TOKEN_BR_OPEN:
            idx, ret_val = Solution.parse_expr(toks, idx+1)
            if idx >= len(toks) or toks[idx][0] != Solution.TOKEN_BR_CLOSE:
                raise Exception(f"no closing bracket {idx}")
            idx += 1
        elif start_tok[0] == Solution.TOKEN_OP and start_tok[1] == '-':
            idx += 1
            if idx >= len(toks):
                raise Exception(f"expression expected after - at {idx}")
            idx, ret_val = Solution.parse_simple(toks, idx)
            ret_val = -1 * ret_val
        else:
            raise Exception(f"symbol not expected {start_tok}")

        #print(f"->simple {idx_start} .. {idx} = {ret_val}- {start_tok}")
        return idx, ret_val

    @staticmethod
    def tokenize(s):
        tokens = re.findall(r"(\(|\)|\+|\-|\d+)", s)
        res = []
        for tok in tokens:
            if tok == '(':
                res.append( (Solution.TOKEN_BR_OPEN, 0) )
            elif tok == ')':
                res.append( (Solution.TOKEN_BR_CLOSE, 0) )
            elif tok == '+' or tok == '-':
                res.append( (Solution.TOKEN_OP, tok) )
            else:
                res.append( (Solution.TOKEN_UINT, int(tok)) )
        return res


