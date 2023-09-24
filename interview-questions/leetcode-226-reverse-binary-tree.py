
# 226. Invert Binary Tree
#
# The description is wrong: 
#
# Given the root of a binary tree, invert the tree, and return its root.
#
#Example 1 shows a breadth first search reversal, whereas only a depth first search reversal is excepted. Please fix the description of the problem, it's really annoying to find a wrong description.
#
#In Example 1 you currently have:
#Input: root = [4,2,7,1,3,6,9]
#Output: [4,7,2,9,6,3,1]
#
#However this result gives you 'wrong answer', whereas the accepted one is
#Input: root = [4,2,7,1,3,6,9]
#Output: [4,2,7,3,1,9,6]
#

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #Solution.revertTree([ root ], 1)
        Solution.revertTreeDFS(root)
        return root

    @staticmethod
    def revertTreeDFS(root):
        if not root:
            return

        Solution.revertTreeDFS(root.left)
        Solution.revertTreeDFS(root.right)

        prev = root.left
        root.left = root.right
        root.right = prev

    @staticmethod
    def revertTreeBFS(nodeLevel, nonNullNodes):
        if nonNullNodes == 0:
            return

        nextLevelNonNullNodes = 0
        nextLevel = []
        for node in nodeLevel:
            if node:
                nextLevel.append(node.left)
                nextLevel.append(node.right)
                if node.left:
                    nextLevelNonNullNodes += 1
                if node.right:
                    nextLevelNonNullNodes += 1
            else:
                nextLevel.append(None)
                nextLevel.append(None)

        Solution.revertTreeBFS(nextLevel, nextLevelNonNullNodes)

        print("--")
        print(f"nodeLevel: {list(map(lambda n: n.val if n else None, nodeLevel))}")
        print(f"nextLevel: {list(map(lambda n: n.val if n else None, nextLevel))}")
        print("###")

        curRevertIdx = len(nextLevel)-1
        for node in nodeLevel:
            if node:
                node.left = nextLevel[curRevertIdx]
                node.right = nextLevel[curRevertIdx-1]
            curRevertIdx -= 2

