# 47. Permutations II
# Medium
#    Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.
#
#
#
#    Example 1:
#
#    Input: nums = [1,1,2]
#    Output:
#    [[1,1,2],
#     [1,2,1],
#     [2,1,1]]
#
#    Example 2:
#
#    Input: nums = [1,2,3]
#    Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ret = []
        num_map = Solution.countEntries(nums)
        Solution.makePerms(num_map, len(nums), [], ret)
        return ret

    def countEntries(nums):
        ret = {}
        for n in nums:
            ret[n] = ret.setdefault(n,0) + 1
        return ret


    def makePerms(num_map, num_len, cur_perm, ret):
        if len(cur_perm) >= num_len:
            ret.append(cur_perm.copy())
            return

        for key in num_map.keys():
            if num_map[key] > 0:
                num_map[key] -= 1
                cur_perm.append(key)
                Solution.makePerms(num_map, num_len, cur_perm, ret)
                cur_perm.pop()
                num_map[key] += 1


