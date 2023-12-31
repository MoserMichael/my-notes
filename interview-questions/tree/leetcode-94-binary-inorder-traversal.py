# 94. Binary Tree Inorder Traversal
# Easy
#
#    Given the root of a binary tree, return the inorder traversal of its nodes' values.
#
#
#
#    Example 1:
#
#    Input: root = [1,null,2,3]
#    Output: [1,3,2]
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
#    Follow up: Recursive solution is trivial, could you do it iteratively?
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Entry:
    STATE_INIT=0
    STATE_VISIT_LEFT=1
    STATE_VISIT_RIGHT=2

    def __init__(self, node):
        self.node = node
        self.state = Entry.STATE_INIT

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.ret = []
        self.norec(root)
        return self.ret


    def norec(self, root):
        if not root:
            return

        stack = [ Entry(root) ]

        while len(stack) != 0:
            top = stack[-1]
            if top.state == Entry.STATE_INIT:
                top.state = Entry.STATE_VISIT_LEFT
                if top.node.left:
                    stack.append( Entry(top.node.left) )
            elif top.state == Entry.STATE_VISIT_LEFT:
                self.ret.append(top.node.val)
                top.state = Entry.STATE_VISIT_RIGHT
                if top.node.right:
                    stack.append( Entry(top.node.right) )
            else:
                stack.pop()



    def rec(self, node):
        if not node:
            return

        self.rec(node.left)
        self.ret.append(node.val)
        self.rec(node.right)



