# 241. Different Ways to Add Parentheses
# Medium
#
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
#
#

#
#    # Intuition
#    Recursive approach. 
#
#    # Approach
#
#    The input is an array of tokens, of the following form
#    ```[num[0], op[0], num[1], op[2], .... num[n] ]```
#
#    The procedure that does the recursion:
#    ```evalAll(self, tokens, idx_from, idx_to):```
#
#    It computes the return the list of values for all expressions that fall in the range of tokens ```tokens[idx_from]``` up until token ```tokens[idx_to]```
#
#    The return value of expressions over a single number is a a list with a single number (bottom case of recursion)
#
#    For all other ranges we need to repeatedly compute the subexpressions
#
#    ```evalAll(tokens,idx_from, cur) evalAll(tokens, cur+2, idx_to)``` where the arithmetic operation is ```tokens[cur+1]```  where ```cur``` is between ```idx_from``` up until ```idx_to```.
#
#    that's quadratic, as each of the invocations is returning a list of values. 
#
#    # Complexity
#    Something complicated. Can come up with a rough upper bound of O(n^3) each recursion level would be quadratic. (but that may be wrong)
#
#    # Code


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







