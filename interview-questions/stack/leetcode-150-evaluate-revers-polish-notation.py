# 150. Evaluate Reverse Polish Notation
# Medium
#    You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.
#
#    Evaluate the expression. Return an integer that represents the value of the expression.
#
#    Note that:
#
#        The valid operators are '+', '-', '*', and '/'.
#        Each operand may be an integer or another expression.
#        The division between two integers always truncates toward zero.
#        There will not be any division by zero.
#        The input represents a valid arithmetic expression in a reverse polish notation.
#        The answer and all the intermediate calculations can be represented in a 32-bit integer.
#
#
#
#    Example 1:
#
#    Input: tokens = ["2","1","+","3","*"]
#    Output: 9
#    Explanation: ((2 + 1) * 3) = 9
#
#    Example 2:
#
#    Input: tokens = ["4","13","5","/","+"]
#    Output: 6
#    Explanation: (4 + (13 / 5)) = 6
#
#    Example 3:
#
#    Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
#    Output: 22
#    Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
#    = ((10 * (6 / (12 * -11))) + 17) + 5
#    = ((10 * (6 / -132)) + 17) + 5
#    = ((10 * 0) + 17) + 5
#    = (0 + 17) + 5
#    = 17 + 5
#    = 22
#
#
#
#    Constraints:
#
#        1 <= tokens.length <= 104
#        tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].
#


#
#    # Intuition
#    Easiest approach is recursive solution. A follow-up question might be: solve the same problem without recursion, therefore do them both.
#
#    # Approach
#
#    General: both solutions use a dictionary ```Solution.map_op_to_handle``` - this one maps the operator token to a function, the function that does the arithmetic operation on two arguments.
#
#    ## Recursive solution: function eval_rec
#    function ```Solution.eval_rec``` receives the input token stack and returns the value of the expression.
#
#    first of all the next symbol is popped off the input stack.
#
#    If it is a number token - that's a terminal node; return the numeric value of the number token.
#
#    For an operation:
#    - evaluate left subexpression and right subexpression. Each of these evaluations is a recursive call to ```Solution.eval_rec``` - on the remaining input, that gets us the arguments for the operation function
#    - get the operation function by lookup from mapping Solution.map_op_to_handle,
#    - apply the operation function on the two arguments, and return the result.
#
#    ## None recursive solution, function eval_no_rec
#
#    Recursive solution has a potential problem: you can run out of stack, if the input stack is too long, so let's do it non recursively.
#
#    The non recursive solution is implemented in function ```Solution.eval_no_rec```
#
#    Non recursive solutions keep all of the data that is kept on the call stack in an explicit stack in main memory. class EntryNonRecursive holds state and data equivalent to one stack frame in the recursive solution.
#
#    - when a new operator is parsed, a new ```EntryNonRecursive``` object to the stack ```eval_stack``` (the member ```op``` is set to operator token, the member ``left`` is None )
#
#    - when a number token is  parsed, convert the string to a number value. Then apply it to the current call stack:
#      - while the stack is not empty, look up the top element in ```eval_stack```
#      - if the ```left`` member is None, then set it to the numeric value (nothing else to to in the loop)
#      - if the ```left``` member is not None, this means we now have both operators for that operator on the top of the stack. Evaluate the top operator
#        - look up the function for the top operator in ```op``` member
#        - pass the ```left`` member and current number as arguments to the operator.
#        - now with the return value, apply it to the same ```eval``` stack - upon the next operation of the loop.
#
#    # Complexity
#    - Time complexity:
#    O(n) where n is number of token.
#
#    - Space complexity:
#    Stack has maximum of n/2 entries, so it's also O(n)
#    # Code
#



class EntryNonRecursive:
    def __init__(self, op):
        self.op = op
        self.left = None

    def __repr__(self):
        return f"[{self.op}({self.left})]"

class Solution:

    map_op_to_handle = { '*' : lambda a,b : int(a * b), 
                         '/' : lambda a,b : int(b / a),
                         '+' : lambda a,b : a + b,
                         '-' : lambda a,b : b - a
                        }

    def evalRPN(self, tokens: List[str]) -> int:
        #return Solution.eval_rec(tokens)
        return Solution.eval_no_rec(tokens)

    
    def eval_no_rec(token_list):
        eval_stack = []

        while True:
            if len(token_list) != 0:
                token = token_list.pop()
                #print(f"token {token} stack {repr(eval_stack)}")
                if token in Solution.map_op_to_handle:
                    eval_stack.append( EntryNonRecursive( token ) )
                else:
                    num = int(token)

                    if not len(eval_stack):
                        return num

                    while True:
                        top_entry = eval_stack[-1]
                        if top_entry.left is None:
                            top_entry.left = num
                            break

                        func = Solution.map_op_to_handle[ top_entry.op ]
                        num = func( top_entry.left, num )
                        eval_stack.pop()

                        if len(eval_stack) == 0:
                            return num
            else:
                assert False        




    def eval_rec(token_list):
        token = token_list.pop()
        if token not in Solution.map_op_to_handle:
            return int(token)
        arg1 = Solution.eval_rec(token_list)
        arg2 = Solution.eval_rec(token_list)

        return Solution.map_op_to_handle[token] (arg1, arg2)
