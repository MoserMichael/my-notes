#230. Kth Smallest Element in a BST
#Medium
#
#Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.
#
# 
#
#Example 1:
#
#Input: root = [3,1,4,null,2], k = 1
#Output: 1
#
#Example 2:
#
#Input: root = [5,3,6,2,4,null,null,1], k = 3
#Output: 3
#
# 
#
#Constraints:
#
#    The number of nodes in the tree is n.
#    1 <= k <= n <= 104
#    0 <= Node.val <= 104
#
# 
#
#Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?
#



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res, _ = Solution.inorder(root, 0, k)
        return res.val

    @staticmethod
    def inorder(root, currentResult, desired):

        res = currentResult
        if not root:
            if desired == 0:
                return root, -1

            return None, 0

        else:

            res, ret = Solution.inorder(root.left, currentResult, desired)
            if res:
                return res, -1

            ret += 1

            if ret + currentResult == desired:
                return root, -1

            res, ret2 = Solution.inorder(root.right, ret + currentResult, desired)
            ret += ret2

            return res, ret


