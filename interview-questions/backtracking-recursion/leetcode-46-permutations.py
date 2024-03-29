# 46. Permutations
# Medium
#Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
#
#
#
#Example 1:
#
#Input: nums = [1,2,3]
#Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#
#Example 2:
#
#Input: nums = [0,1]
#Output: [[0,1],[1,0]]
#
#Example 3:
#
#Input: nums = [1]
#Output: [[1]]
#
#
#
#Constraints:
#
#    1 <= nums.length <= 6
#    -10 <= nums[i] <= 10
#    All the integers of nums are unique.
#


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        outPermutations = []
        #Solution.permuteRec(nums, [], outPermutations)
        Solution.permuteFast(nums, [False] * len(nums),  [], outPermutations)
        return outPermutations

    @staticmethod
    def permuteFast(nums, inUseArray, res, out):

        #print(f"nums {nums} res {res}")
        if len(res) == len(nums):
            #print(f"-> {res}")
            out.append(res.copy())
            return


        for i in range(0, len(nums)):
            if not inUseArray[i]:
                inUseArray[i] = True
                res.append(nums[i])
                Solution.permuteFast( nums, inUseArray, res, out)
                res.pop()
                inUseArray[i] = False


    @staticmethod
    def permuteRec(nums, res, out):

        #print(f"nums {nums} res {res}")
        if not len(nums):
            #print(f"-> {res}")
            out.append(res.copy())
            return


        for i in range(0, len(nums)):
            rem = nums.pop(i)
            res.append(rem)
            Solution.permuteRec( nums, res, out)
            res.pop()
            nums.insert(i, rem)


