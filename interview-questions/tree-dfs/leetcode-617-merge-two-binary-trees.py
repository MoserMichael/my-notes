# 617. Merge Two Binary Trees
# Easy
#
#    You are given two binary trees root1 and root2.
#
#    Imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not. You need to merge the two trees into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of the new tree.
#
#    Return the merged tree.
#
#    Note: The merging process must start from the root nodes of both trees.
#
#     
#
#    Example 1:
#
#    Input: root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
#    Output: [3,4,5,5,4,null,7]
#
#    Example 2:
#
#    Input: root1 = [1], root2 = [1,2]
#    Output: [2,2]
#
#     
#
#    Constraints:
#
#        The number of nodes in both trees is in the range [0, 2000].
#        -104 <= Node.val <= 104
#
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        return Solution.doMerge(root1, root2)

    def doMerge(t1, t2):
        if not t1 and not t2:
            return None

        val = 0
        if t1:
            val += t1.val
        if t2:
            val += t2.val

        node = TreeNode(val)

        node.left = Solution.doMerge(t1.left if t1 else None, t2.left if t2 else None)
        node.right = Solution.doMerge(t1.right if t1 else None, t2.right if t2 else None)

        return node

        
