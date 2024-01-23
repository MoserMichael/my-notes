# 783. Minimum Distance Between BST Nodes
# Easy
#
#    Given the root of a Binary Search Tree (BST), return the minimum difference between the values of any two different nodes in the tree.
#
#     
#
#    Example 1:
#
#    Input: root = [4,2,6,1,3]
#    Output: 1
#
#    Example 2:
#
#    Input: root = [1,0,48,null,null,12,49]
#    Output: 1
#
#     
#
#    Constraints:
#
#        The number of nodes in the tree is in the range [2, 100].
#        0 <= Node.val <= 105
#
#


# Intuition
depth first traversal of the tree. Each call returns the maximum and minimum value of the subtrees.

For each node we compute the difference between the node value and the maximum  of the left subtree, and the difference between the minimum of the right subtree and he node value - and udpate the minimum difference, if any of these values are smaller than the current minimum


# Complexity
- Time complexity:
$$O(V + E)$$ - each tree node and link is traversed

- Space complexity:
$$O(log n)$$ - counting the stack size, and assuming that the tree is half-way balanced.


import math

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        self.min_dist = math.inf
        self.bfs(root)
        return self.min_dist

    def bfs(self, node):
        if not node.left and not node.right:
            return node.val, node.val
        
        min_val = max_val = 0
        if node.left:
            min_val, rmax_val = self.bfs(node.left)
            self.min_dist = min(self.min_dist, node.val - rmax_val)
        else:
            min_val = node.val

        if node.right:
            rmin_val, max_val = self.bfs(node.right)
            self.min_dist = min(self.min_dist, rmin_val - node.val)
        else:
            max_val = node.val

        return min_val, max_val

        
