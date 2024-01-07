# 331. Verify Preorder Serialization of a Binary Tree
# Medium
#
#    One way to serialize a binary tree is to use preorder traversal. When we encounter a non-null node, we record the node's value. If it is a null node, we record using a sentinel value such as '#'.
#
#    For example, the above binary tree can be serialized to the string "9,3,4,#,#,1,#,#,2,#,6,#,#", where '#' represents a null node.
#
#    Given a string of comma-separated values preorder, return true if it is a correct preorder traversal serialization of a binary tree.
#
#    It is guaranteed that each comma-separated value in the string must be either an integer or a character '#' representing null pointer.
#
#    You may assume that the input format is always valid.
#
#        For example, it could never contain two consecutive commas, such as "1,,3".
#
#    Note: You are not allowed to reconstruct the tree.
#
#
#
#    Example 1:
#
#    Input: preorder = "9,3,4,#,#,1,#,#,2,#,6,#,#"
#    Output: true
#
#    Example 2:
#
#    Input: preorder = "1,#"
#    Output: false
#
#    Example 3:
#
#    Input: preorder = "9,#,#,1"
#    Output: false
#
#
#
#    Constraints:
#
#        1 <= preorder.length <= 104
#        preorder consist of integers in the range [0, 100] and '#' separated by commas ','.
#


#  
#  Use a stack to follow through the serialization process. 
#  A stack entry stands for a tree node that is being restored. It pushes a new entry, whenever a new tre nodes appears in the input.
#  The state of a stack entry is VISIT_LEFT, when it is pushed to the stack.
#  An stack entry is popped off the stack, when a tree node in the input is followed by two null entries (#).
#  in this case we examine the top of the stack repeatedly, if the state of the stack entry is VISIT_LEFT then it is changed to VISIT_RIGHT, and break from loop
#  if the state of the stack is VISIT_RIGHT, then it means that right subtree has been completed, in this case the last stack entry is popped off the stack.
#  This process is repeated in a loop.
#  Also take care of input tokens trailing after the end of input or token stream ending prematurely, before the stack has been reduced to empty.


class Solution:
    VISIT_LEFT=1
    VISIT_RIGHT=2


    def isValidSerialization(self, preorder: str) -> bool:

        if preorder == "#":
            return True

        stack = []
        isEof = False

        for tok in preorder.split(","):
            if isEof:
                return False

            if tok == "#":
                if len(stack) == 0:
                    return False # tokens on trailing end

                if stack[-1] == Solution.VISIT_LEFT:
                    stack[-1] = Solution.VISIT_RIGHT
                else:
                    stack.pop()
                    while True:
                        if len(stack) == 0:
                            break
                        if stack[-1] == Solution.VISIT_LEFT:
                            stack[-1] = Solution.VISIT_RIGHT
                            break
                        stack.pop()
                    if len(stack) == 0:
                        isEof = True
            else:
                stack.append(Solution.VISIT_LEFT)

        return len(stack) == 0
