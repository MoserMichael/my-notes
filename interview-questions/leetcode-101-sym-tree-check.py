#Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
#Easy
# 
#
#Example 1:
#
#Input: root = [1,2,2,3,4,4,3]
#Output: true
#
#Example 2:
#
#Input: root = [1,2,2,null,3,null,3]
#Output: false
#
# 
#
#Constraints:
#
#    The number of nodes in the tree is in the range [1, 1000].
#    -100 <= Node.val <= 100
#
# 
#Follow up: Could you solve it both recursively and iteratively?
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return Solution.bfs( [root], 1 if root else 0)

    @staticmethod
    def bfs(level, nonNullNodes):
        if nonNullNodes == 0:
            return True
        nextLevel = []

        if not Solution.isSym(level):
            return False

        nonNullNodesNextLevel = 0
        for node in level:
            if node:
                nextLevel.append(node.left)
                nextLevel.append(node.right)
                if node.left:
                    nonNullNodesNextLevel += 1
                if node.right:
                    nonNullNodesNextLevel += 1
            else:
                nextLevel.append(None)
                nextLevel.append(None)

        return Solution.bfs(nextLevel, nonNullNodesNextLevel)

    @staticmethod
    def isSym(level):

        pos = 0
        revPos = len(level) - 1

        while pos < revPos:
            if not level[pos] or not level[revPos]:
                if level[pos] or level[revPos]:
                    return False
            else:
                if level[pos].val != level[revPos].val:
                    return False
            pos += 1
            revPos -= 1

        return True
