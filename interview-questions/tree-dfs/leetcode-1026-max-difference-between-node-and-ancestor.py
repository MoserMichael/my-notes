# 1026. Maximum Difference Between Node and Ancestor
# Medium
#
#    Given the root of a binary tree, find the maximum value v for which there exist different nodes a and b where v = |a.val - b.val| and a is an ancestor of b.
#
#    A node a is an ancestor of b if either: any child of a is equal to b or any child of a is an ancestor of b.
#
#     
#
#    Example 1:
#
#    Input: root = [8,3,10,1,6,null,14,null,null,4,7,13]
#    Output: 7
#    Explanation: We have various ancestor-node differences, some of which are given below :
#    |8 - 3| = 5
#    |3 - 7| = 4
#    |8 - 1| = 7
#    |10 - 13| = 3
#    Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.
#
#    Example 2:
#
#    Input: root = [1,null,2,null,0,3]
#    Output: 3
#
#     
#
#    Constraints:
#
#        The number of nodes in the tree is in the range [2, 5000].
#        0 <= Node.val <= 105
#


#    Intuition
#
#    Finding the maximum difference between two nodes, where one node is the ancestor of the other involves depth first search traversal of the tree. For each path you need to maintain the maximum and minimum value of any of the nodes along the path. Now the difference between the maximum and minimum values is the biggest possible difference betweeen any of the nodes. at each step compute that difference, and update the maximum if the value exceeds the current maximum.
#    Complexity
#
#        Time complexity:
#        O(n)O(n)O(n) traversing every node in the tree.
#
#        Space complexity:
#        O(logn)O(log n)O(logn) if the tree is not a list.
#

import math

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.max_diff = -math.inf
        self.rec(root, -math.inf, math.inf)
        return self.max_diff

    def rec(self, cur, max_val, min_val):
        if not cur:
           return
        max_val = max(max_val, cur.val)
        min_val = min(min_val, cur.val)
        
        self.max_diff = max(self.max_diff, max_val - min_val)
        self.rec(cur.left, max_val, min_val)
        self.rec(cur.right, max_val, min_val)
        
