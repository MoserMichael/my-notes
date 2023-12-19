# 530. Minimum Absolute Difference in BST
# Easy
#Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.
#
#
#
#Example 1:
#
#Input: root = [4,2,6,1,3]
#Output: 1
#
#Example 2:
#
#Input: root = [1,0,48,null,null,12,49]
#Output: 1
#
#
#
#Constraints:
#
#    The number of nodes in the tree is in the range [2, 104].
#    0 <= Node.val <= 105
#
#


import math

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.minDiff = math.inf    
        self.walkBFS(root)
        return self.minDiff

    def walkBFS(self, root):
        if not root:
            return -1, -1

        left_min, left_max = self.walkBFS(root.left)
        right_min, right_max = self.walkBFS(root.right)

        #print(f"root: {root.val} left_max: {left_max} right_max {right_max}")

        if left_max != -1:
            diff = root.val - left_max
            if diff < self.minDiff:
                self.minDiff = diff
    
        if right_min != -1:
            diff = right_min - root.val
            if diff < self.minDiff:
                self.minDiff = diff
    
        if left_min == -1:
            left_min = root.val
        if right_max == -1:
            right_max = root.val

        print(f"-> minDiff {self.minDiff}")

        return left_min, right_max

        

