# 993. Cousins in Binary Tree
# Easy
#    Given the root of a binary tree with unique values and the values of two different nodes of the tree x and y, return true if the nodes corresponding to the values x and y in the tree are cousins, or false otherwise.
#
#    Two nodes of a binary tree are cousins if they have the same depth with different parents.
#
#    Note that in a binary tree, the root node is at the depth 0, and children of each depth k node are at the depth k + 1.
#
#
#
#    Example 1:
#
#    Input: root = [1,2,3,4], x = 4, y = 3
#    Output: false
#
#    Example 2:
    #
#    Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
#    Output: true
#
#    Example 3:
#
#    Input: root = [1,2,3,null,4], x = 2, y = 3
#    Output: false
#
#
#
#    Constraints:
#
#        The number of nodes in the tree is in the range [2, 100].
#        1 <= Node.val <= 100
#        Each node has a unique value.
#        x != y
#        x and y are exist in the tree.
#


#    # Intuition
#    breadth first search
#
#    # Approach
#    while filling in the list of next level nodes, check for the two values in the values of the next level. If both were found then check if parent is different.
#
#    How would that compare to DFS approach?
#    - would be faster for the average case, if nodes are not too deep.
#    - needs more memory than DFS.
#
#    # Complexity
#    - Time complexity:
#    O(n) - n number of nodes. all nodes are visited in worst case
#
#    - Space complexity:
#    O(n) - need to keep list of next level node.
#
#    # Code


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class EntryInfo:
    def __init__(self, num):
        self.num = num
        self.found = False
        self.parent = None

class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:

        if root is None:
            return False

        if x == root.val or y == root.val:
            return False

        entries = [ EntryInfo(x), EntryInfo(y) ]

        level=[root]
        while len(level) != 0:

            next_level = []
            found_in_level = 0

            for node in level:
                if node.left:
                    found_in_level += Solution.check(node.left.val, node, entries)
                    next_level.append(node.left)
                if node.right:
                    found_in_level += Solution.check(node.right.val, node, entries)
                    next_level.append(node.right)

            if found_in_level == 1:
                return False
            if found_in_level == 2:
                return entries[0].parent.val != entries[1].parent.val

            level = next_level

        return False

    def check(n, parent, entries):

        for entry in entries:
            if entry.num == n:
                entry.found = True
                entry.parent = parent
                return 1
        return 0


