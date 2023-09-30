# 3Sum
# Medium
#Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
#
#Notice that the solution set must not contain duplicate triplets.
#
#
#
#Example 1:
#
#Input: nums = [-1,0,1,2,-1,-4]
#Output: [[-1,-1,2],[-1,0,1]]
#Explanation:
#nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
#nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
#nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
#The distinct triplets are [-1,0,1] and [-1,-1,2].
#Notice that the order of the output and the order of the triplets does not matter.
#
#Example 2:
#
#Input: nums = [0,1,1]
#Output: []
#Explanation: The only possible triplet does not sum up to 0.
#
#Example 3:
#
#Input: nums = [0,0,0]
#Output: [[0,0,0]]
#Explanation: The only possible triplet sums up to 0.
#
#
#
#Constraints:
#
#    3 <= nums.length <= 3000
#    -105 <= nums[i] <= 105
#


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        solutions = set()
        map_val_to_idx={}

        new_nums = []

        for idx in range(0, len(nums)):
            val = nums[idx]

            if val not in map_val_to_idx:
                map_val_to_idx[val]=[]
                repeat_count = 0
            else:
                repeat_count = len(map_val_to_idx[val])

            if repeat_count < 3:
                new_idx = len(new_nums)
                map_val_to_idx[val].append(new_idx)
                new_nums.append(val)

        for idx_low in range(0, len(new_nums)):
            for idx_high in range(0, len(new_nums)):
                if idx_low == idx_high:
                    continue

                complement = 0 - new_nums[idx_low] - new_nums[idx_high]
                complement_idx_list = map_val_to_idx.get(complement)

                if complement_idx_list:
                    solution = [complement, new_nums[idx_low], new_nums[idx_high]]
                    solution.sort()
                    solution_tup = tuple(solution)

                    if solution_tup not in solution:
                        for num in complement_idx_list:
                            if num != idx_low and num != idx_high:
                                solutions.add( solution_tup )

        return list(solutions)

