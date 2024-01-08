# 736. Parse Lisp Expression
# Hard
#
#    You are given a string expression representing a Lisp-like expression to return the integer value of.
#
#    The syntax for these expressions is given as follows.
#
#        An expression is either an integer, let expression, add expression, mult expression, or an assigned variable. Expressions always evaluate to a single integer.
#        (An integer could be positive or negative.)
#        A let expression takes the form "(let v1 e1 v2 e2 ... vn en expr)", where let is always the string "let", then there are one or more pairs of alternating variables and expressions, meaning that the first variable v1 is assigned the value of the expression e1, the second variable v2 is assigned the value of the expression e2, and so on sequentially; and then the value of this let expression is the value of the expression expr.
#        An add expression takes the form "(add e1 e2)" where add is always the string "add", there are always two expressions e1, e2 and the result is the addition of the evaluation of e1 and the evaluation of e2.
#        A mult expression takes the form "(mult e1 e2)" where mult is always the string "mult", there are always two expressions e1, e2 and the result is the multiplication of the evaluation of e1 and the evaluation of e2.
#        For this question, we will use a smaller subset of variable names. A variable starts with a lowercase letter, then zero or more lowercase letters or digits. Additionally, for your convenience, the names "add", "let", and "mult" are protected and will never be used as variable names.
#        Finally, there is the concept of scope. When an expression of a variable name is evaluated, within the context of that evaluation, the innermost scope (in terms of parentheses) is checked first for the value of that variable, and then outer scopes are checked sequentially. It is guaranteed that every expression is legal. Please see the examples for more details on the scope.
#
#
#
#    Example 1:
#
#    Input: expression = "(let x 2 (mult x (let x 3 y 4 (add x y))))"
#    Output: 14
#    Explanation: In the expression (add x y), when checking for the value of the variable x,
#    we check from the innermost scope to the outermost in the context of the variable we are trying to evaluate.
#    Since x = 3 is found first, the value of x is 3.
#
#    Example 2:
#
#    Input: expression = "(let x 3 x 2 x)"
#    Output: 2
#    Explanation: Assignment in let statements is processed sequentially.
#
#    Example 3:
#
#    Input: expression = "(let x 1 y 2 x (add x y) (add x y))"
#    Output: 5
#    Explanation: The first (add x y) evaluates as 3, and is assigned to x.
#    The second (add x y) evaluates as 3+2 = 5.
#
#
#
#    Constraints:
#
#        1 <= expression.length <= 2000
#        There are no leading or trailing spaces in expression.
#        All tokens are separated by a single space in expression.
#        The answer and all intermediate calculations of that answer are guaranteed to fit in a 32-bit integer.
#        The expression is guaranteed to be legal and evaluate to an integer.
#
#


#    # Intuition
#    Parse the lisp s-expr into an abstract syntax tree, where each node stands for a different kind of operation. All of the abstract syntax tree nodes have an eval method. Evaluation of an expresion results to a call of the eval method of a node in the abstract syntax tree; this first evaluates all of the nested nodes - these are the arguements required for the evaluation the current node, then performs the desired evaluation defined by the current node.
#
#    Now the eval method receives the current scope object. A scope object can return the value of variables. The evaluation of a let expression is creating its own context object, as it can introduce variable bindings during its evaluation. Now each context object is pointing to the context object of the enclosing let expression - this way you can resolve the variable values correctly.
#
#    # Approach
#    This exercise was fun.
#

class Scope:
    def __init__(self, parent = None):
        self.ctx = {}
        self.parent = parent

    def get(self, name):
        rt = self.ctx.get(name)
        if rt is not None:
            #print(f"var {name} {rt}")
            return rt
        if self.parent:
            return self.parent.get(name)
        raise Exception(f"can't lookup {name}")

class Expr:

    def eval(self, bindings):
        return None

class NumberPrimaryExpr(Expr):
    def __init__(self, numberOrVar):
        self.numberOrVar = numberOrVar

    def eval(self, scope):
        if type(self.numberOrVar) == int:
            return self.numberOrVar
        return scope.get(self.numberOrVar)

    def __repr__(self):
        if type(self.numberOrVar) == int:
            return f"{self.numberOrVar}"
        return f"{self.numberOrVar}"

class SimpleExpr(Expr):
    def __init__(self, op):
        self.op = op
        self.e1 = None
        self.e2 = None

    def eval(self, scope):
        if self.op == 'mult':
            a1 = self.e1.eval(scope)
            a2 = self.e2.eval(scope)
            rt = a1 * a2
        elif self.op == 'add':
            a1 = self.e1.eval(scope)
            a2 = self.e2.eval(scope)
            rt = a1 + a2
        else:
            raise Exception(f"{self.op} not supported")

        #print(f"{self.op}: {rt} = {a1} {self.op} {a2}")
        return rt

    def __repr__(self):
        return f"({self.op} {self.e1} {self.e2})"


class LetExpr(Expr):
    def __init__(self):
        self.expr = None
        self.bindings = []

    def eval(self, parent_scope):
        scope = Scope(parent_scope)
        for b in self.bindings:
            scope.ctx[ b[0] ] = b[1].eval(scope)
        return self.expr.eval(scope)

    def __repr__(self):
        rt = "(let "
        for b in self.bindings:
            rt += f"({b[0]} {b[1]}) "

        rt += f"{self.expr})"
        return rt

class Solution:
    TOK_NUM = 1
    TOK_BR_OPEN = 2
    TOK_BR_CLOSE = 3
    TOK_KEYW = 4
    TOK_IDENTIF = 5

    def evaluate(self, expression: str) -> int:
        self.pos = 0
        self.token = Solution.getToken(expression)

        scope = Scope()
        ast = self.parse()
        assert ast is not None
        #print(f"{ast}")
        return ast.eval(scope)

    def parse(self):
        rt = None
        if self.tok()[0] == Solution.TOK_BR_OPEN:
            self.pos += 1
            if self.tok()[0] == Solution.TOK_KEYW:
                val = self.tok()[1]
                if val == 'mult' or val == 'add':
                    self.pos += 1
                    rt = SimpleExpr(val)
                    rt.e1 = self.parse()
                    rt.e2 = self.parse()
                elif val == 'let':
                    rt = LetExpr()
                    self.pos += 1
                    while self.tok()[0] != Solution.TOK_BR_CLOSE:
                        if  self.tok()[0] == Solution.TOK_IDENTIF and self.next_tok()[0] != Solution.TOK_BR_CLOSE:
                            idval = self.tok()[1]
                            self.pos += 1
                            e = self.parse()
                            rt.bindings.append( ( idval, e ) )
                        else:
                            e = self.parse()
                            rt.expr = e

            assert self.tok()[0] == Solution.TOK_BR_CLOSE
            self.pos += 1

        else:
            if self.tok()[0] == Solution.TOK_NUM or self.tok()[0] == Solution.TOK_IDENTIF:
                rt = NumberPrimaryExpr(self.tok()[1])
                self.pos += 1

        return rt

    def tok(self):
        return self.token[self.pos]

    def next_tok(self):
        return self.token[self.pos+1]

    def getToken(exp):
        ret=[]
        for tokst in re.findall(r'\(|\)|\-?\d+|\w+',exp):
            if tokst == '(':
                ret.append( ( Solution.TOK_BR_OPEN, None))
            elif tokst == ')':
                ret.append( ( Solution.TOK_BR_CLOSE, None))
            elif tokst.lstrip('-').isdigit():
                ret.append( ( Solution.TOK_NUM, int(tokst) ) )
            elif tokst == 'add' or tokst == 'mult' or tokst == 'let':
                ret.append( ( Solution.TOK_KEYW, tokst ) )
            else:
                ret.append( ( Solution.TOK_IDENTIF, tokst ) )

        #print(ret)
        return ret




