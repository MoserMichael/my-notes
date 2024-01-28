# 1609. Even Odd Tree
# Medium
#    A binary tree is named Even-Odd if it meets the following conditions:
#
#        The root of the binary tree is at level index 0, its children are at level index 1, their children are at level index 2, etc.
#        For every even-indexed level, all nodes at the level have odd integer values in strictly increasing order (from left to right).
#        For every odd-indexed level, all nodes at the level have even integer values in strictly decreasing order (from left to right).
#
#    Given the root of a binary tree, return true if the binary tree is Even-Odd, otherwise return false.
#
#     
#
#    Example 1:
#
#    Input: root = [1,10,4,3,null,7,9,12,8,6,null,null,2]
#    Output: true
#    Explanation: The node values on each level are:
#    Level 0: [1]
#    Level 1: [10,4]
#    Level 2: [3,7,9]
#    Level 3: [12,8,6,2]
#    Since levels 0 and 2 are all odd and increasing and levels 1 and 3 are all even and decreasing, the tree is Even-Odd.
#
#    Example 2:
#
#    Input: root = [5,4,2,3,3,7]
#    Output: false
#    Explanation: The node values on each level are:
#    Level 0: [5]
#    Level 1: [4,2]
#    Level 2: [3,3,7]
#    Node values in level 2 must be in strictly increasing order, so the tree is not Even-Odd.
#
#    Example 3:
#
#    Input: root = [5,9,1,3,5,7]
#    Output: false
#    Explanation: Node values in the level 1 should be even integers.
#
#     
#
#    Constraints:
#
#        The number of nodes in the tree is in the range [1, 105].
#        1 <= Node.val <= 106
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        level = [ root ]
        num_level = 0

        while len(level) != 0:

            #print(f"level {num_level % 2}", list(map(lambda e : e.val, level)))

            if num_level %2 == 0:
                # even index level
                if not Solution.check_odd_increasing(level):
                    return False
            else:
                if not Solution.check_even_decreasing(level):
                    return False

            next_level = []
            for node in level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            level = next_level
            num_level += 1

        return True

    def check_odd_increasing(level):
        prev_val = -math.inf
        for node in level:
            if node.val % 2 != 1:
                return False
            if node.val <= prev_val:
                return False
            prev_val = node.val

        return True

    def check_even_decreasing(level):
        prev_val = math.inf
        for node in level:
            if node.val % 2 != 0:
                return False
            if node.val >= prev_val:
                return False
            prev_val = node.val
        return True
