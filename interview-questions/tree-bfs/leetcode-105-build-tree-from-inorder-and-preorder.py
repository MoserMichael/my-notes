# 105. Construct Binary Tree from Preorder and Inorder Traversal
# Medium
#Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.
#
#
#
#Example 1:
#
#Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
#Output: [3,9,20,null,null,15,7]
#
#Example 2:
#
#Input: preorder = [-1], inorder = [-1]
#Output: [-1]
#
#
#
#Constraints:
#
#    1 <= preorder.length <= 3000
#    inorder.length == preorder.length
#    -3000 <= preorder[i], inorder[i] <= 3000
#    preorder and inorder consist of unique values.
#    Each value of inorder also appears in preorder.
#    preorder is guaranteed to be the preorder traversal of the tree.
#    inorder is guaranteed to be the inorder traversal of the tree.
#





# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        return Solution.buildRec(preorder, inorder)


    def buildRec(preorder, inorder):

        if len(inorder) == 0:
            return None

        root = preorder[0]
        ret = TreeNode(root)

        inOrderSet = set()
        for inOrderIdx in range(0, len(inorder)):
            if inorder[inOrderIdx] == root:
                break
            inOrderSet.add(inorder[inOrderIdx])

        #preOrderRest = preorder[1:]
        #preOrderLeft = list(filter(lambda x : x in inOrderSet, preOrderRest))
        #preOrderRight = list(filter(lambda x : x not in inOrderSet, preOrderRest))

        preOrderRight = []
        preOrderLeft = []
        for n in preorder[1:]:
            if n in inOrderSet:
                preOrderLeft.append(n)
            else:
                preOrderRight.append(n)


        ret.left = Solution.buildRec(preOrderLeft,inorder[0:inOrderIdx])

        ret.right = Solution.buildRec(preOrderRight, inorder[inOrderIdx+1:])

        return ret
