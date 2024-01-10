# 897. Increasing Order Search Tree
# Easy
#
#    Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only one right child.
#
#
#
#    Example 1:
#
#    Input: root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
#    Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]
#
#    Example 2:
#
#    Input: root = [5,1,7]
#    Output: [1,null,5,null,7]
#
#
#
#    Constraints:
#
#        The number of nodes in the given tree will be in the range [1, 100].
#        0 <= Node.val <= 1000
#
#

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        return Solution.onePass(root)
        #return Solution.simple(root)

    def onePass(root):
        f,l = Solution.onePassRec(root)
        
        return f

    def onePassRec(root):
        if not root:
            return None, None

        leftFirst, leftLast = Solution.onePassRec(root.left)
        rightFirst, rightLast = Solution.onePassRec(root.right)

        retFirst = retLast = None

        if leftFirst:
            retFirst = leftFirst
            leftLast.right = root
        else:
            retFirst = root

        if rightFirst:
            root.right = rightFirst
            retLast = rightLast
        else:
            root.right = None
            retLast = root

        root.left = None

        return retFirst, retLast
        
        


    def simple(root):
        ret = []
        Solution.inorder(root, ret)

        for idx, it in enumerate(ret):
            it.left = None
            if idx < len(ret)-1:
                it.right = ret[idx+1]
            else:
                it.right = None

        return ret[0]

    def inorder(root, ret):
        if not root:
            return None
        Solution.inorder(root.left, ret)
        ret.append(root)
        Solution.inorder(root.right, ret)
         

