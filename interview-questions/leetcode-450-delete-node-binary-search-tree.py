# 450. Delete Node in a BST
# Medium
#Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.
#
#Basically, the deletion can be divided into two stages:
#
#    Search for a node to remove.
#    If the node is found, delete the node.
#
# 
#
#Example 1:
#
#Input: root = [5,3,6,2,4,null,7], key = 3
#Output: [5,4,6,2,null,null,7]
#Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
#One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
#Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.
#
#Example 2:
#
#Input: root = [5,3,6,2,4,null,7], key = 0
#Output: [5,3,6,2,4,null,7]
#Explanation: The tree does not contain a node with value = 0.
#
#Example 3:
#
#Input: root = [], key = 0
#Output: []
#
# 
#
#Constraints:
#
#    The number of nodes in the tree is in the range [0, 104].
#    -105 <= Node.val <= 105
#    Each node has a unique value.
#    root is a valid binary search tree.
#    -105 <= key <= 105
#
# 
#
#Follow up: Could you solve it with time complexity O(height of tree)?
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        r, v = Solution.imp(root, key)
        if v:
            return r
        return root

    @staticmethod
    def imp(root, key):
        if not root:
            return None, False
        if root.val == key:
            # delete key
            if root.right:
                Solution.insertLeftMost(root.right, root.left)
                return root.right, True
            if root.left:
                Solution.insertRightMost(root.left, root.right)
                return root.left, True
            return None, True
        
        if root.val > key:
            r, v = Solution.imp( root.left, key)
            if v:
                root.left = r
        
        if root.val < key:
            r, v = Solution.imp( root.right, key)
            if v:
                root.right = r

        return None, False
        
    @staticmethod
    def insertLeftMost(root, toInsert):
        if not toInsert:
            return root, False
        if not root:
            return toInsert, True
        
        r, v = Solution.insertLeftMost(root.left, toInsert)
        if v:
            root.left = toInsert

        return None, False

    @staticmethod
    def insertRightMost(root, toInsert):
        if not toInsert:
            return root, False
        if not root:
            return toInsert, True
        
        r, v = Solution.insertRightMost(root.right, toInsert)
        if v:
            root.right = toInsert

        return None, False
        
        
            




        
