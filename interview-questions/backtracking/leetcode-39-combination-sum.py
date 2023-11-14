# 39. Combination Sum
# Medium
#    Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.
#
#    The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the
#    frequency
#    of at least one of the chosen numbers is different.
#
#    The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.
#
#
#
#    Example 1:
#
#    Input: candidates = [2,3,6,7], target = 7
#    Output: [[2,2,3],[7]]
#    Explanation:
#    2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
#    7 is a candidate, and 7 = 7.
#    These are the only two combinations.
#
#    Example 2:
#
#    Input: candidates = [2,3,5], target = 8
#    Output: [[2,2,2,2],[2,3,3],[3,5]]
#
#    Example 3:
#
#    Input: candidates = [2], target = 1
#    Output: []
#
#
#
#    Constraints:
#
#        1 <= candidates.length <= 30
#        2 <= candidates[i] <= 40
#        All elements of candidates are distinct.
#        1 <= target <= 40
#
#

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        Solution.res = []
        Solution.cur_res = []

        Solution.rec(candidates, target, 0, 0)

        return Solution.res

    def rec(cand, target, pos, path_sum):

        if pos >= len(cand):
            return

        cur_num = 0
        orig_len = len(Solution.cur_res)

        while target >= cur_num:

            if target ==  cur_num:
                Solution.res.append(Solution.cur_res.copy())
                break

            Solution.rec(cand, target - cur_num, pos+1, path_sum + cur_num)

            Solution.cur_res.append(cand[pos])
            cur_num += cand[pos]

        if orig_len != len(Solution.cur_res):
            Solution.cur_res = Solution.cur_res[0 : orig_len ]

