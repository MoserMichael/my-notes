# 100. Same Tree
# Easy
#Given the roots of two binary trees p and q, write a function to check if they are the same or not.
#
#Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
#
# 
#
#Example 1:
#
#Input: p = [1,2,3], q = [1,2,3]
#Output: true
#
#Example 2:
#
#Input: p = [1,2], q = [1,null,2]
#Output: false
#
#Example 3:
#
#Input: p = [1,2,1], q = [1,1,2]
#Output: false
#
# 
#
#Constraints:
#
#    The number of nodes in both trees is in the range [0, 100].
#    -104 <= Node.val <= 104
#



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return Solution.imp(p, q)

    @staticmethod
    def imp(p, q):

        if p is None and q is None:
            return True

        if p is not None and q is not None:
            #print(f"init: {p.val} {q.val}")

            res1 = int(p.left is not None) ^ int(q.left is not None)
            res2 = int(p.right is not None) ^ int(q.right is not None)
            if not res1 and not res2:
                nodeValCmp = p.val == q.val

                #print(f"{p.val} {q.val} -> {nodeValCmp}")

                return nodeValCmp and Solution.imp(p.left, q.left) and Solution.imp(p.right, q.right)

        return False


