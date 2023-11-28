# 2641. Cousins in Binary Tree II
# Medium
#
#    Given the root of a binary tree, replace the value of each node in the tree with the sum of all its cousins' values.
#
#    Two nodes of a binary tree are cousins if they have the same depth with different parents.
#
#    Return the root of the modified tree.
#
#    Note that the depth of a node is the number of edges in the path from the root node to it.
#
#
#
#    Example 1:
#
#    Input: root = [5,4,9,1,10,null,7]
#    Output: [0,0,0,7,7,null,11]
#    Explanation: The diagram above shows the initial binary tree and the binary tree after changing the value of each node.
#    - Node with value 5 does not have any cousins so its sum is 0.
#    - Node with value 4 does not have any cousins so its sum is 0.
#    - Node with value 9 does not have any cousins so its sum is 0.
#    - Node with value 1 has a cousin with value 7 so its sum is 7.
#    - Node with value 10 has a cousin with value 7 so its sum is 7.
#    - Node with value 7 has cousins with values 1 and 10 so its sum is 11.
#
#    Example 2:
#
#    Input: root = [3,1,2]
#    Output: [0,0,0]
#    Explanation: The diagram above shows the initial binary tree and the binary tree after changing the value of each node.
#    - Node with value 3 does not have any cousins so its sum is 0.
#    - Node with value 1 does not have any cousins so its sum is 0.
#    - Node with value 2 does not have any cousins so its sum is 0.
#
#
#
#    Constraints:
#
#        The number of nodes in the tree is in the range [1, 105].
#        1 <= Node.val <= 104
#


#    # Intuition
#    breadth first traversal of tree.
#
#    # Approach
#    breadth first traversal of tree maintains a list of nodes in the current level.
#
#    Now with each node, keep a tuple that contains the node and its parent node. Also maintain the sum of all the node values.
#
#    To compute the sibling value: sum the value of the node and its sibling, substract the sum of all values from the sum of the siblings. set the siblings value to this result.
#
#    # Complexity
#    - Time complexity:
#    O(n) n is the number of tree nodes, we visit all tree nodes.
#
#    - Space complexity:
#    O(n) - the list of the last level has n/2 elements
#

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        sum_all = root.val
        level = [ (root, None) ]

        while len(level) != 0:

            Solution.processLevel(level, sum_all)

            nextLevel = []
            sum_all_next = 0

            for entry in level:
                node = entry[0]
                if node.left:
                    nextLevel.append( (node.left, node) )
                    sum_all_next += node.left.val

                if node.right:
                    nextLevel.append( (node.right, node) )
                    sum_all_next += node.right.val

            level = nextLevel
            sum_all = sum_all_next

        return root

    def processLevel(level, sum_all):

        idx = 0
        while idx < len(level):
            if idx+1 < len(level) and level[idx][1] == level[idx+1][1]:
                # two siblings
                sibling_sum = level[idx][0].val + level[idx+1][0].val

                level[idx][0].val = level[idx+1][0].val = sum_all - sibling_sum
                idx += 2
            else:
                # one sibling
                sibling_sum = level[idx][0].val
                level[idx][0].val = sum_all - sibling_sum
                idx += 1






