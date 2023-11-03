# 111. Minimum Depth of Binary Tree
# Medium
#Given a binary tree, find its minimum depth.
#
#The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
#
#Note: A leaf is a node with no children.
#
#
#
#Example 1:
#
#Input: root = [3,9,20,null,null,15,7]
#Output: 2
#
#Example 2:
#
#Input: root = [2,null,3,null,4,null,5,null,6]
#Output: 5
#
#
#
#Constraints:
#
#    The number of nodes in the tree is in the range [0, 105].
#    -1000 <= Node.val <= 1000
#



# Intuition
Let's do both the recursive solution and stack based solution.

#    # Approach
#    Recursive solution ```Solution.rec```
#    - for Null node case return 0 as minimum depth of binary tree
#    - compute the solution for left and right subtrees
#        - if both left and right subtree exist, return 1 + min(left-subtree-val, right-subtree-val)  - adding one to consider the current node.
#       - if eithe left or right subtree is null: return 1 + maximum solution of left and right subgtree
#
#
#    Stack based solution ```Solution.stack``` maintains a stack explicitly. (variable ```st```).
#     - start with a stack that includes the root node entry in ```VISIT_LEFT``` state.
#     - if at the top of the stack there is a Null node, in this case we have a solution for both left and subtree. The action starts here: we want to find a solution to the parent nodes as well, if possible.
#        - Loop
#            - get depth at current level of stack, pop the top entry off stack
#            - if stack is empty - we got the solution, Return it.
#            - in top entry in stack is in ```VISIT_LEFT``` state, assign the depth field to current computed value, set ```VISIT_RIGHT``` state and break from loop.
#            - if entry is in ```VISIT_RIGHT``` state, now we have the solution for both left and right subtree. Compute the solution for the current node: if we have a not zero solution for the left subtree and the value for right subtree is also not zero - get set solution for current node as 1 + min(left-subtree-solution, right-subtree-solution), if either one of them is empty set it as 1 + max(left-subtree-solution, right-subtree-solution.)
#    - Now that we managed to reduce the stack, expand the stack, a node needs to.
#         - if top entry is in ```VISIT_LEFT``` state - push a new stack entry for the node of left subtree (the new node is initially in  ```VISIT_LEFT``` state)
#         - if top entry is in ```VISIT_RIGHT``` state - push a new stack entry for the node of right subtree (the new node is initially in  ```VISIT_LEFT``` state)
#
#
#    # Complexity
#    - Time complexity:
#    $$O(n)$$ - visiting each tree node twice.
#
#    - Space complexity: $$$(O(log(n)))$$$ - stack has the depth of the tree in the medium case.
#
#    # Code

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Entry:
    VISIT_LEFT=0
    VISIT_RIGHT=1

    def __init__(self, node):
        self.node = node
        self.depth = 0
        self.state = Entry.VISIT_LEFT

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        return Solution.rec(root)
        #return Solution.stack(root)



    def stack(node):
        st = [ Entry(node) ]

        while True:
            top = st[-1]

            if not top.node:
                # action starts here
                while True:
                    depth = st[-1].depth
                    st.pop()
                    if len(st) == 0:
                        return depth        
                    
                    top = st[-1]
                    if top.state == Entry.VISIT_LEFT:
                        top.depth = depth
                        top.state = Entry.VISIT_RIGHT
                        break
                    else:
                        # wrap up.
                        if top.depth != 0 and depth != 0:
                            top.depth = 1 + min(top.depth, depth)
                        else:
                            top.depth = 1 + max(top.depth, depth)

            if top.state == Entry.VISIT_LEFT:
                st.append( Entry(top.node.left) )
            elif top.state == Entry.VISIT_RIGHT:
                st.append( Entry(top.node.right) )
            else:
                assert False

                
    def rec(node):
        if not node:
            return 0
        l = Solution.rec(node.left)
        r = Solution.rec(node.right)

        if r != 0 and l != 0:
            m = min(r,l)
        else:
            m = max(r,l)

        return 1 + m
