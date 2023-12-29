# 572. Subtree of Another Tree
# Easy
#
#    Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.
#
#    A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.
#
#
#
#    Example 1:
#
#    Input: root = [3,4,5,1,2], subRoot = [4,1,2]
#    Output: true
#
#    Example 2:
#
#    Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
#    Output: false
#
#
#
#    Constraints:
#
#        The number of nodes in the root tree is in the range [1, 2000].
#        The number of nodes in the subRoot tree is in the range [1, 1000].
#        -104 <= root.val <= 104
#        -104 <= subRoot.val <= 104
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return Solution.recWalk(root, subRoot)

    def recWalk(root, subroot):
        if not root:
            return False
        if Solution.check(root, subroot):
            return True
        if Solution.recWalk(root.left, subroot) or Solution.recWalk(root.right, subroot):
            return True
        return False


    def check(root, subroot):
        if not root and not subroot:
            return True

        if root.val != subroot.val:
            return False

        if root.left is None and subroot.left is not None:
            return False
        if root.left is not None and subroot.left is None:
            return False

        if root.right is None and subroot.right is not None:
            return False
        if root.right is not None and subroot.right is None:
            return False

        return Solution.check(root.left, subroot.left) and Solution.check(root.right, subroot.right)

