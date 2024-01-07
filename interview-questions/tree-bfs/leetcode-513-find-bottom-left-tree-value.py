# 513. Find Bottom Left Tree Value
# Medium
#
#    Given the root of a binary tree, return the leftmost value in the last row of the tree.
#
#
#
#    Example 1:
#
#    Input: root = [2,1,3]
#    Output: 1
#
#    Example 2:
#
#    Input: root = [1,2,3,4,null,5,6,null,null,7]
#    Output: 7
#
#
#
#    Constraints:
#
#        The number of nodes in the tree is in the range [1, 104].
#        -231 <= Node.val <= 231 - 1
#


#    # Intuition
#    BFS traversal, here we fill a list with the nodes that make up the next level, then make the next level into the current level.
#
#    When next level is empty, then get to the current(previous) level
#    and return the value of the first element.
#
#
#    # Complexity
#    - Time complexity:
#    $$O(n)$$ where n is the number onodes in the tree
#
#    - Space complexity:
#    $$O(n)$$ - the length of the last level for a fully balanced tree is n/2+1 or something like that.
#

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:

        # BFS traversal. when next level is empty, then get to the current(previous) level
        # and return the value of the first element.

        level = [root]
        while True:
            # fill next level
            next_level = []
            for node in level:
                if node.left is not None:
                    next_level.append(node.left)
                if node.right is not None:
                    next_level.append(node.right)

            if len(next_level) == 0:
                return level[0].val

            level = next_level

