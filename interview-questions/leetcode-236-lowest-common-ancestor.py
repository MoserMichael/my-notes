# 236. Lowest Common Ancestor of a Binary Tree
# Medium
#Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
#
#According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
#
#
#
#Example 1:
#
#Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
#Output: 3
#Explanation: The LCA of nodes 5 and 1 is 3.
#
#Example 2:
#
#Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
#Output: 5
#Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
#
#Example 3:
#
#Input: root = [1,2], p = 1, q = 2
#Output: 1
#
#
#
#Constraints:
#
#    The number of nodes in the tree is in the range [2, 105].
#    -109 <= Node.val <= 109
#    All Node.val are unique.
#    p != q
#    p and q will exist in the tree.
#
#



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        r, _ = Solution.imp(root, p, q)
        return r

    @staticmethod
    def imp(root, p, q):
        if not root:
            return None, 0

        r1, v1 = Solution.imp(root.left, p, q);
        if r1:
            return r1, 0

        r2, v2 = Solution.imp(root.right, p, q)
        if r2:
            return r2, 0

        if v1 and v2:
            return root, None

        found = False
        if root.val == p.val or root.val == q.val:
            found = True

        if found and (v1 or v2):
            return root, None

        return None, found or v1 or v2





