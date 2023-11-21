# 235. Lowest Common Ancestor of a Binary Search Tree
# Medium
#
#    Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.
#
#    According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
#
#     
#
#    Example 1:
#
#    Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
#    Output: 6
#    Explanation: The LCA of nodes 2 and 8 is 6.
#
#    Example 2:
#
#    Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
#    Output: 2
#    Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
#
#    Example 3:
#
#    Input: root = [2,1], p = 2, q = 1
#    Output: 2
#
#     
#
#    Constraints:
#
#        The number of nodes in the tree is in the range [2, 105].
#        -109 <= Node.val <= 109
#        All Node.val are unique.
#        p != q
#        p and q will exist in the BST.
#
#



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #return Solution.slow(root, p, q)
        return Solution.fast(root, p, q)


    def fast(root, p, q):
        pos_p = root
        pos_q = root

        while pos_p and pos_q:
            if pos_p.val != pos_q.val:
                break
            last_common = pos_p

            if p.val > pos_p.val:
                pos_p = pos_p.right
            elif p.val < pos_p.val:
                pos_p = pos_p.left
            else:
                break

            if q.val > pos_q.val:
                pos_q = pos_q.right
            elif q.val < pos_q.val:
                pos_q = pos_q.left
            else:
                break

        return last_common

    def slow(root, p, q):
        path_p = Solution.find(root, p, [])
        path_q = Solution.find(root, q, [])

        last_common = root

        idx = 0
        while True:
            if idx == len(path_p) or idx == len(path_q):
                break
            if path_p[idx].val == path_q[idx].val:
                last_common = path_p[idx]
            else:
                break
            idx += 1


        return last_common


    def find(node, to_find, path):
        if not node:
            return []
        path.append(node)
        if node.val == to_find.val:
            return path

        if node.val > to_find.val:
            return Solution.find(node.left, to_find, path)
        else:
            return Solution.find(node.right, to_find, path)

