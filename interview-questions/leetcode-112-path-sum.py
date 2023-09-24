#112. Path Sum
#Easy
#Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.
#
#A leaf is a node with no children.
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        return Solution.imp(root, 0, targetSum)

    @staticmethod
    def imp(root, sumSoFar, targetSum):
        if not root:
            return False

        nextVal = sumSoFar + root.val

        if root.left is None and root.right is None:
            return nextVal == targetSum

        return Solution.imp( root.left, nextVal, targetSum) or Solution.imp( root.right, nextVal, targetSum)


