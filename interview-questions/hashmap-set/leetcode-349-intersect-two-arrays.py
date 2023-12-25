# 349. Intersection of Two Arrays
# Easy
#
#    Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.
#
#    Example 1:
#
#    Input: nums1 = [1,2,2,1], nums2 = [2,2]
#    Output: [2]
#
#    Example 2:
#
#    Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
#    Output: [9,4]
#    Explanation: [4,9] is also accepted.
#
#
#
#    Constraints:
#
#        1 <= nums1.length, nums2.length <= 1000
#        0 <= nums1[i], nums2[i] <= 1000
#

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) < len(nums2):
            return Solution.intersect(nums2, nums1)
        return Solution.intersect(nums1, nums2)

    def intersect(larger, smaller):
        small_map={}
        ret = []

        for n in smaller:
            small_map[n] = 0

        for n in larger:

            if n in small_map and small_map[n] == 0:
                ret.append(n)
                small_map[n] = 1

        return ret

