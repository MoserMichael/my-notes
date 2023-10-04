# 117. Populating Next Right Pointers in Each Node II
# Medium
#Given a binary tree
#
#struct Node {
#  int val;
#  Node *left;
#  Node *right;
#  Node *next;
#}
#
#Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
#
#Initially, all next pointers are set to NULL.
#
#
#
#Example 1:
#
#Input: root = [1,2,3,4,5,null,7]
#Output: [1,#,2,3,#,4,5,7,#]
#Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
#
#Example 2:
#
#Input: root = []
#Output: []
#
#
#
#Constraints:
#
#    The number of nodes in the tree is in the range [0, 6000].
#    -100 <= Node.val <= 100
#
#
#
#Follow-up:
#
#    You may only use constant extra space.
#    The recursive approach is fine. You may assume implicit stack space does not count as extra space for this problem.
#
#



"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        Solution.space_constant_bfs(root)
        #Solution.simple([root])
        return root

    @staticmethod
    def space_constant_bfs(first_in_level):
        next_first_in_level = prev = None

        node = first_in_level
        while node:
            if node.left:
                if prev is None:
                    next_first_in_level = prev = node.left
                else:
                    prev.next = node.left
                    prev = node.left

            if node.right:
                if prev is None:
                    next_first_in_level = prev = node.right
                else:
                    prev.next = node.right
                    prev = node.right

            node = node.next

        if next_first_in_level:
            Solution.space_constant_bfs(next_first_in_level)

    @staticmethod
    def simple(level):
        next_level=[]
        for node in level:
            if node:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

        if len(next_level) != 0:
            for idx in range(0, len(next_level)-1):
                node = next_level[idx]
                next_node = next_level[idx+1]
                node.next = next_node

            Solution.simple(next_level)



