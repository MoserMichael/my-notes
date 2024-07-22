#1530. Number of Good Leaf Nodes Pairs
#Medium
#    You are given the root of a binary tree and an integer distance. A pair of two different leaf nodes of a binary tree is said to be good if the length of the shortest path between them is less than or equal to distance.
#
#    Return the number of good leaf node pairs in the tree.
#
#
#
#    Example 1:
#
#    Input: root = [1,2,3,null,4], distance = 3
#    Output: 1
#    Explanation: The leaf nodes of the tree are 3 and 4 and the length of the shortest path between them is 3. This is the only good pair.
#
#    Example 2:
#
#    Input: root = [1,2,3,4,5,6,7], distance = 3
#    Output: 2
#    Explanation: The good pairs are [4,5] and [6,7] with shortest path = 2. The pair [4,6] is not good because the length of ther shortest path between them is 4.
#
#    Example 3:
#
#    Input: root = [7,1,4,6,null,5,3,null,null,null,null,null,2], distance = 3
#    Output: 1
#    Explanation: The only good pair is [2,5].
#
#
#
#    Constraints:
#
#        The number of nodes in the tree is in the range [1, 210].
#        1 <= Node.val <= 100
#        1 <= distance <= 10
#

import collections

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        numPairs=0

        def dfs(elm):
            nonlocal distance, numPairs

            left_leafs = []
            right_leafs = []

            if elm.right:
                left_leafs = list(map(lambda val : val+1, dfs(elm.right)))
            if elm.left:
                right_leafs = list(map(lambda val : val+1, dfs(elm.left)))

            if not elm.left and not elm.right:
                left_leafs.append(0)
                return left_leafs

            left_idx=0

            while left_idx < len(left_leafs):
                right_idx = 0
                to_add = 0
                while right_idx < len(right_leafs) and left_leafs[left_idx] + right_leafs[right_idx] <= distance:
                    to_add += 1
                    right_idx += 1
                numPairs += to_add
                if to_add == 0:
                    break
                left_idx += 1

            ret = left_leafs + right_leafs
            ret.sort()
            #print(f"{elm.val} -> {ret}")
            return ret

        dfs(root)
        return numPairs
