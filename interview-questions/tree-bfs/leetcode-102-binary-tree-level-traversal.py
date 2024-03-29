# 102. Binary Tree Level Order Traversal
# Medium
#    Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
#
#
#
#    Example 1:
#
#    Input: root = [3,9,20,null,null,15,7]
#    Output: [[3],[9,20],[15,7]]
#
#    Example 2:
#
#    Input: root = [1]
#    Output: [[1]]
#
#    Example 3:
#
#    Input: root = []
#    Output: []
#
#
#
#    Constraints:
#
#        The number of nodes in the tree is in the range [0, 2000].
#        -1000 <= Node.val <= 1000
#



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        ret = []
        Solution.level([root], ret)
        return ret

    def level(level, ret):
        if len(level) == 0:
            return

        ret.append( map( lambda node : node.val, level ) )
        next_level = []
        for node in level:
            if node.left is not None:
                next_level.append(node.left)
            if node.right is not None:
                next_level.append(node.right)

        Solution.level(next_level, ret)
