# 108. Convert Sorted Array to Binary Search Tree
# Easy
#Given an integer array nums where the elements are sorted in ascending order, convert it to a
#height-balanced
#binary search tree.
#
#
#
#Example 1:
#
#Input: nums = [-10,-3,0,5,9]
#Output: [0,-3,9,-10,null,5]
#Explanation: [0,-10,5,null,-3,null,9] is also accepted:
#
#Example 2:
#
#Input: nums = [1,3]
#Output: [3,1]
#Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.
#
#
#
#Constraints:
#
#    1 <= nums.length <= 104
#    -104 <= nums[i] <= 104
#    nums is sorted in a strictly increasing order.
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        #nums.sort()
        return Solution.buildTree(nums)



    @staticmethod
    def buildTree(sequence):
        if len(sequence) == 0:
            return None
        if len(sequence) == 1:
            return TreeNode(sequence[0])

        mid_point = int(len(sequence)/2)
        #print(f"mid_point {mid_point} len: {len(sequence)}")

        ret = TreeNode(sequence[mid_point])

        ret.left = Solution.buildTree(sequence[0:mid_point])
        ret.right = Solution.buildTree(sequence[mid_point+1:])

        return ret

