# 22. Generate Parentheses
# Medium
#Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
#
#
#
#Example 1:
#
#Input: n = 3
#Output: ["((()))","(()())","(())()","()(())","()()()"]
#
#Example 2:
#
#Input: n = 1
#Output: ["()"]
#
#
#
#Constraints:
#
#    1 <= n <= 8
#



class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ret = []
        Solution.generateRec("", 0, n, ret)
        return ret

    @staticmethod
    def generateRec(stack_str, open_parenthesis, parenthesis_left, out_array):
        if parenthesis_left == 0:
            if open_parenthesis > 0:
                stack_str += ")" * open_parenthesis
            out_array.append(stack_str)
            return

        Solution.generateRec(stack_str + "(", open_parenthesis+1, parenthesis_left-1, out_array)

        if open_parenthesis:
            Solution.generateRec(stack_str + ")", open_parenthesis-1, parenthesis_left, out_array)





