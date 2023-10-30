# 1361. Validate Binary Tree Nodes
# Medium
#You have n binary tree nodes numbered from 0 to n - 1 where node i has two children leftChild[i] and rightChild[i], return true if and only if all the given nodes form exactly one valid binary tree.
#
#If node i has no left child then leftChild[i] will equal -1, similarly for the right child.
#
#Note that the nodes have no values and that we only use the node numbers in this problem.
#
#
#
#Example 1:
#
#Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,-1,-1,-1]
#Output: true
#
#Example 2:
#
#Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,3,-1,-1]
#Output: false
#
#Example 3:
#
#Input: n = 2, leftChild = [1,0], rightChild = [-1,-1]
#Output: false
#
#
#
#Constraints:
#
#    n == leftChild.length == rightChild.length
#    1 <= n <= 104
#    -1 <= leftChild[i], rightChild[i] <= n - 1
#


#    # Intuition
#    Description doesn't tell you: you don't know which node is the root, need to find that out.
#
#    # Approach
#    Each node can be the root of a subtree. The function ```Solution.dfs``` traverses such a subtree, It returns two return values, first a boolean  value - ```True``` if no cycles have been found - that means this node is the root of a valid subtree; the second return value is the number of nodes in that subtree. 
#
#    The function ```Solution.dfs``` is traversing a tree in depth first search order, upon each call a ```visited``` set is maintained. The ```visited``` set helps to exclude cycles - if a node has already been visited, then we have a cycle. The solution also maintains a map ```part_of_tree``` that maps the node value to the number of nodes in the tree. If a node has already been visited by a previous call to ```Solution.dfs``` then we can tell the number of nodes in tht subtree. (this trick is called memoization)
#
#    the main function is ```Solution.validateBinaryTreeNodes```. It calls ```Solution.dfs``` on each node. If a cycle has been found (fist return value of Solution.dfs is False) then this is clearly not a tree, return ```False```. If no cycles have been found, and the number of nodes in the tree is equal to the total number of nodes, then we just found and traversed the root node. If none of the nodes is a root that covers all of the nodes, then return ```False```
#
#
#    # Complexity
#    - Time complexity:
#    O(n) - visiting each node
#
#    - Space complexity:
#    O(n) the meoization map has an entry for each node
#
#    # Code

class Solution:

    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:

        part_of_tree = {}
        for idx in range(0,len(leftChild)):
            if idx == 0 or ((leftChild[idx] != -1 or rightChild[idx] != -1)and idx not in visited):

                visited = set()
                ret, num_nodes = Solution.dfs(idx, leftChild, rightChild, visited, part_of_tree)
                if not ret:
                    return False
                if num_nodes == n:
                    return True
                
                part_of_tree[idx] = num_nodes
                if len(part_of_tree) == n:
                    return True

        return False


    def dfs(node, leftChild, rightChild, visited, part_of_tree):
        if node == -1:
            return True, 0
        if node in visited:
            return False, -1
        if node in part_of_tree:
            return True, part_of_tree[node]
        visited.add(node)
        
        r, rn = Solution.dfs(rightChild[node], leftChild, rightChild, visited, part_of_tree) 
        if not r:
            return False, -1
        l, ln = Solution.dfs(leftChild[node], leftChild, rightChild, visited, part_of_tree)
        if not l:
            return False, -1
        return True, rn + ln + 1

