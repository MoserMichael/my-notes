# 144. Binary Tree Preorder Traversal
# Easy
#
#    Given the root of a binary tree, return the preorder traversal of its nodes' values.
#
#
#
#    Example 1:
#
#    Input: root = [1,null,2,3]
#    Output: [1,2,3]
#
#    Example 2:
#
#    Input: root = []
#    Output: []
#
#    Example 3:
#
#    Input: root = [1]
#    Output: [1]
#
#
#
#    Constraints:
#
#        The number of nodes in the tree is in the range [0, 100].
#        -100 <= Node.val <= 100
#
#
#
#    Follow up: Recursive solution is trivial, could you do it iteratively?
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class StackEntry:
    MODE_INIT = 0
    MODE_VISIT_LEFT = 1
    MODE_VISIT_RIGHT = 2

    def __init__(self, mode, node):
        self.mode = mode
        self.node = node

class Solution:



    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = [ StackEntry(StackEntry.MODE_INIT, root) ]
        ret = []

        while len(stack) != 0:
            top = stack[-1]
            if top.node is None:
                stack.pop()
                continue

            node = top.node

            if top.mode == StackEntry.MODE_INIT:
                ret.append(node.val)
                top.mode = StackEntry.MODE_VISIT_LEFT
                stack.append( StackEntry(StackEntry.MODE_INIT, node.left) )
            elif top.mode == StackEntry.MODE_VISIT_LEFT:
                top.mode = StackEntry.MODE_VISIT_RIGHT
                stack.append( StackEntry(StackEntry.MODE_INIT, node.right) )
            else:
                stack.pop()

        return ret
