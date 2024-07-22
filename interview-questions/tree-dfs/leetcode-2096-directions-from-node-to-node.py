#2096. Step-By-Step Directions From a Binary Tree Node to Another
#Medium
#    You are given the root of a binary tree with n nodes. Each node is uniquely assigned a value from 1 to n. You are also given an integer startValue representing the value of the start node s, and a different integer destValue representing the value of the destination node t.
#
#    Find the shortest path starting from node s and ending at node t. Generate step-by-step directions of such path as a string consisting of only the uppercase letters 'L', 'R', and 'U'. Each letter indicates a specific direction:
#
#        'L' means to go from a node to its left child node.
#        'R' means to go from a node to its right child node.
#        'U' means to go from a node to its parent node.
#
#    Return the step-by-step directions of the shortest path from node s to node t.
#
#     
#
#    Example 1:
#
#    Input: root = [5,1,2,3,null,6,4], startValue = 3, destValue = 6
#    Output: "UURL"
#    Explanation: The shortest path is: 3 → 1 → 5 → 2 → 6.
#
#    Example 2:
#
#    Input: root = [2,1], startValue = 2, destValue = 1
#    Output: "L"
#    Explanation: The shortest path is: 2 → 1.
#
#     
#
#    Constraints:
#
#        The number of nodes in the tree is n.
#        2 <= n <= 105
#        1 <= Node.val <= n
#        All the values in the tree are unique.
#        1 <= startValue, destValue <= n
#        startValue != destValue
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:

        def rec(node, nodeToFind, path ):
            if not node:
                return False
            if node.val == nodeToFind:
                return True
            fnd = rec(node.right, nodeToFind, path)
            if fnd:
                path.appendleft( (node.val, 'R' ) )
                return True
            fnd = rec(node.left, nodeToFind, path)
            if fnd:
                path.appendleft( (node.val, 'L' ) )
                return True, 
            
            return False
            
        pathStart, pathDest = deque(), deque()    
        r1 = rec(root, startValue, pathStart)
        r2 = rec(root, destValue, pathDest)

        if not r1 or not r2:
            return ""

        #print(f"pstart {pathStart} pdest {pathDest}")

        pos = 0
        while True:

            if pos >= len(pathDest) or pos >= len(pathStart):
                #print(f"found-short: {pos}")

                if len(pathStart) > len(pathDest):
                    return 'U' * (len(pathStart) - pos)
                
                return 'U' * (len(pathStart)-pos-1) + "".join(map(lambda entry: entry[1], list(pathDest)[pos:]))

            if pathStart[pos] != pathDest[pos]:
                #print(f"found: {pos}")
                return 'U' * (len(pathStart)-pos) + "".join(map(lambda entry: entry[1], list(pathDest)[pos:]))
        
            pos += 1

        return ""


        
            

