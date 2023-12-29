# 90. Subsets II
# Medium
#
#    Given an integer array nums that may contain duplicates, return all possible
#    subsets
#    (the power set).
#
#    The solution set must not contain duplicate subsets. Return the solution in any order.
#
#
#
#    Example 1:
#
#    Input: nums = [1,2,2]
#    Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
#
#    Example 2:
#
#    Input: nums = [0]
#    Output: [[],[0]]
#
#
#
#    Constraints:
#
#        1 <= nums.length <= 10
#        -10 <= nums[i] <= 10
#


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ret = set()
        Solution.rec(nums,0, [], ret)
        return list(ret)

    def rec(nums, idx, current_set, ret):
        if idx == len(nums):
            cp = current_set.copy()
            cp.sort()
            ret.add( tuple( cp ) )
            return

        Solution.rec(nums, idx+1,current_set, ret)

        current_set.append(nums[idx])
        Solution.rec(nums, idx+1,current_set, ret)
        current_set.pop()

