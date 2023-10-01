# 103. Binary Tree Zigzag Level Order Traversal
# Medium
#Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).
#
# 
#
#Example 1:
#
#Input: root = [3,9,20,null,null,15,7]
#Output: [[3],[20,9],[15,7]]
#
#Example 2:
#
#Input: root = [1]
#Output: [[1]]
#
#Example 3:
#
#Input: root = []
#Output: []
#
# 
#
#Constraints:
#
#    The number of nodes in the tree is in the range [0, 2000].
#    -100 <= Node.val <= 100
#



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ret_list = []
        if root:
            Solution.bfs([root], True, ret_list)
        return ret_list


    @staticmethod
    def bfs(level, reportDir, resultList):
        if len(level) == 0:
            return

        ret = []
        nextLevel = []

        if reportDir:
            for node in level:
                if node:
                    ret.append(node.val)
        else:
            for node in level[::-1]:
                if node:
                    ret.append(node.val)

        for node in level:
            if node:
                if node.left:
                    nextLevel.append(node.left)

                if node.right:
                    nextLevel.append(node.right)

        resultList.append(ret)

        Solution.bfs(nextLevel, not reportDir, resultList)
