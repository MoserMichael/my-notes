# 222. Count Complete Tree Nodes
# Easy (?)
#Given the root of a complete binary tree, return the number of the nodes in the tree.
#
#According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.
#
#Design an algorithm that runs in less than O(n) time complexity.
#
#
#
#Example 1:
#
#Input: root = [1,2,3,4,5,6]
#Output: 6
#
#Example 2:
#
#Input: root = []
#Output: 0
#
#Example 3:
#
#Input: root = [1]
#Output: 1
#
#
#
#Constraints:
#
#    The number of nodes in the tree is in the range [0, 5 * 104].
#    0 <= Node.val <= 5 * 104
#    The tree is guaranteed to be complete.
#



import math

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return Solution.rec(root, 1, 1)

    # advanced solution - less than O(n) !!! (that's not easy!!!)
    # it's O(log(n)*O(log(n))) - is that less than O(n) ?
    @staticmethod
    def rec(root, level, nodesOnCurrentLevel):

        if not root.left and not root.right:
            #print(f"return: level {level} curLevel {nodesOnCurrentLevel}")
            return int(math.pow(2, (level-1))) -1 + nodesOnCurrentLevel
            #return root.val

        if not root.right:
            return Solution.rec(root.left, level+1, 2 * nodesOnCurrentLevel - 1)

        d1 = Solution.depthLeft(root)
        d2 = 1+Solution.depthLeft(root.right)

        #print(f"root: {root.val} d1 {d1} d2 {d2} | level: {level} curLevel {nodesOnCurrentLevel}")

        if d1 == d2:
            return Solution.rec(root.right, level+1,  2 * nodesOnCurrentLevel)
        if d1 >= d2:
            return Solution.rec(root.left, level+1,  2 * nodesOnCurrentLevel - 1)
        assert(False)   

    def depthLeft(root):
        if not root:
            return 0
        return 1 + Solution.depthLeft(root.left)

    # the 'easy' solution is O(n) - but the question asks for less than O(n)
    @staticmethod
    def naive(root):
        if not root:
            return 0
        return 1 + Solution.naive(root.left) + Solution.naive(root.right)

