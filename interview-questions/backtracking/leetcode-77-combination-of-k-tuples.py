# 77. Combinations
# Medium
#Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].
#
#You may return the answer in any order.
#
#
#
#Example 1:
#
#Input: n = 4, k = 2
#Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
#Explanation: There are 4 choose 2 = 6 total combinations.
#Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.
#
#Example 2:
#
#Input: n = 1, k = 1
#Output: [[1]]
#Explanation: There is 1 choose 1 = 1 total combination.
#
#
#
#Constraints:
#
#    1 <= n <= 20
#    1 <= k <= n
#

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k > n:
            return []
        result = []
        Solution.comb(n+1, 0, k, [], result)
        return result

    @staticmethod
    def comb(max_num, cur_max, num_left, combination, result):
        if num_left == 0:
            result.append(combination.copy())
            return

        for idx in range(cur_max+1, max_num-num_left+1):
            combination.append(idx)
            Solution.comb(max_num, idx, num_left-1, combination, result)
            combination.pop()

