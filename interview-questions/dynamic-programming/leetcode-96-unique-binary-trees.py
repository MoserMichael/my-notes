# 96. Unique Binary Search Trees
# Medium
#    Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.
#
#
#
#    Example 1:
#
#    Input: n = 3
#    Output: 5
#
#    Example 2:
#
#    Input: n = 1
#    Output: 1
#
#
#
#    Constraints:
#
#        1 <= n <= 19
#


#    # Intuition
#    The first intuition was to enumerate all of the possible trees and count them. But wait, the picture says that there is a recurrency relationship (that mans that the number of trees num[tree_size] can be expressed by means of combining the tree sizes for smaller sizes). If this is the case, then the same task can be solved by means of dynamic programming.
#
#    # Approach
#    The recurrency relationship:
#    for a tree with size ```TreeSize``` you can have ```Left``` nodes on the left subtree and ```Right``` nodes on the right subtree, where
#        ```TreeSize``` = ```Left``` + ```Right``` + 1
#
#    Now for the number of combinations ```NumComb``` you have
#
#    For any given combination of left and right nodes, you need to multiply the number of combinations on the left subtree by the number of combinations on the right tree. Now sum these expressions for all of the possible sizes of the left and right subtrees, you get the following expression:
#
#    ```NumComb(n) = NumComb(n) + NumComb(n-1-1) NumComb(1) * NumComb(n-1-2) NumComb(2) + .... NumComb(1) NumComb(n-1-1) * NumComb(n-1-2) + NumComb(n)```
#
#    Now given the recurrency relation, lets write the dynamic programming solution: Create a table for the intermediate results, the tree of size one has exactly one combination.
#
#    ```
#     arr = [0] * (n+1)
#
#     arr[1] = 1
#    ```
#
#     for a given tree size ```n``` first compute the tree sizes smaller than n, in the outer loop. The inner loop computes the recurrency formulat - it computes the number of combinations for tree size n from the already computed values for the smaller trees.
#
#    ```
#     for idx in range(2, len_iter+1):
#        sm = 0
#        for size_left in range(0,idx):
#            size_right = idx - 1 - size_left
#            if arr[size_left] != 0 and arr[size_right] != 0:
#                add_size = arr[size_left] * arr[size_right]
#            else:
#                add_size =  max(arr[size_left], arr[size_right])
#                sm += 2 * add_size
#
#            arr[idx] = sm
#    ```
#    The last step is to return the result, that is the size of the largest tree
#    ```
#            return arr[-1]
#    ```
#    # Complexity
#    - Time complexity:
#    O(size_of_tree*2) - there is an inner loop here that is on the size of the current iteration.
#
#    - Space complexity:
#    O(size_of_tree)
#
#    # Code
#

class Solution:
    def numTrees(self, n: int) -> int:
        arr = [0] * (n+1)

        arr[1] = 1

        for idx in range(2, len(arr)):
            sm = 0

            for size_left in range(0,idx):
                size_right = idx - 1 - size_left
                if arr[size_left] != 0 and arr[size_right] != 0:
                    add_size = arr[size_left] * arr[size_right]
                else:
                    add_size =  max(arr[size_left], arr[size_right])
                sm += add_size

            arr[idx] = sm
            #print(f"res: {sm} arr: - {arr}")

        return arr[-1]

