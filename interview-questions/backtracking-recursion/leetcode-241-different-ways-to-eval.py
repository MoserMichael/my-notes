# 241. Different Ways to Add Parentheses
# Medium
#    Given a string expression of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. You may return the answer in any order.
#
#    The test cases are generated such that the output values fit in a 32-bit integer and the number of different results does not exceed 104.
#
#
#
#    Example 1:
#
#    Input: expression = "2-1-1"
#    Output: [0,2]
#    Explanation:
#    ((2-1)-1) = 0
#    (2-(1-1)) = 2
#
#    Example 2:
#
#    Input: expression = "2*3-4*5"
#    Output: [-34,-14,-10,-10,10]
#    Explanation:
#    (2*(3-(4*5))) = -34
#    ((2*3)-(4*5)) = -14
#    ((2*(3-4))*5) = -10
#    (2*((3-4)*5)) = -10
#    (((2*3)-4)*5) = 10
#
#
#
#    Constraints:
#
#        1 <= expression.length <= 20
#        expression consists of digits and the operator '+', '-', and '*'.
#        All the integer values in the input expression are in the range [0, 99].
#        The integer values in the input expression do not have a leading '-' or '+' denoting the sign.
#


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        # this works, there are no negative numbers in the input
        # per conditions
        tokens = re.findall(r'\d+|\+|\-|\*|\\', expression)

        # all strings to numbers, convert strings to numbers
        for idx in range(0,len(tokens)):
            if (idx+1) % 2 == 1:
                tokens[idx] = int(tokens[idx])

        self.memo = {}
        self.res = []

        r = self.evalAll(tokens, 0, len(tokens)-1)

        return r


    def evalAll(self, tokens, idx_from, idx_to):
        #assert idx_from <= idx_to

        key = f"{idx_from}-{idx_to}"
        if key in self.memo:
            return self.memo[key]

        ret = []
        if idx_from == idx_to:
            #assert isinstance( tokens[idx_from], int)
            ret.append(tokens[idx_from])
        else:
            for idx_cur in range(idx_from, idx_to-1, 2) :
                first_half = self.evalAll(tokens, idx_from, idx_cur)
                second_half = self.evalAll(tokens, idx_cur+2, idx_to)
                assert len(first_half) > 0
                assert len(second_half) > 0

                for a in first_half:
                    for b in second_half:
                        r = Solution.comp(tokens[idx_cur+1], a, b)
                        ret.append(r)

        self.memo[ key ] = ret
        return ret


    def comp(op, val1, val2):
        if op == '*':
            return val1 * val2
        if op == '/':
            return val1 / val2
        if op == '+':
            return val1 + val2
        if op == '-':
            return val1 - val2
        assert False





