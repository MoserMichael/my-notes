# 145. Binary Tree Postorder Traversal
# Easy
#
#    Given the root of a binary tree, return the postorder traversal of its nodes' values.
#
#
#
#    Example 1:
#
#    Input: root = [1,null,2,3]
#    Output: [3,2,1]
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
#        The number of the nodes in the tree is in the range [0, 100].
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
    INIT = 0
    VISIT_LEFT = 1
    VISIT_RIGHT = 2
    VISIT_NODE = 3

    def __init__(self, node):
        self.node = node
        self.state = Entry.INIT

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.ret = []
        self.norec(root)
        #self.rec(root)
        return self.ret

    def norec(self, root):
        if not root:
            return

        stack = [ Entry(root) ]

        while len(stack) != 0:
            entry = stack[-1]
            if entry.state == Entry.INIT:
                entry.state = Entry.VISIT_LEFT
                if entry.node.left:
                    stack.append( Entry(entry.node.left) )
                    continue

            if entry.state == Entry.VISIT_LEFT:
                entry.state = Entry.VISIT_RIGHT
                if entry.node.right:
                    stack.append( Entry(entry.node.right) )
                    continue

            if entry.state == Entry.VISIT_RIGHT:
                self.ret.append(entry.node.val)
                stack.pop()


    def rec(self, root):
        if not root:
            return
        self.rec(root.left)
        self.rec(root.right)
        self.ret.append(root.val)




