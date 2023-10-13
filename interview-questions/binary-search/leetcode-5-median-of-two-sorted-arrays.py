# 4. Median of Two Sorted Arrays
# Hard
#Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
#
#The overall run time complexity should be O(log (m+n)).
#
#
#
#Example 1:
#
#Input: nums1 = [1,3], nums2 = [2]
#Output: 2.00000
#Explanation: merged array = [1,2,3] and median is 2.
#
#Example 2:
#
#Input: nums1 = [1,2], nums2 = [3,4]
#Output: 2.50000
#Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
#
#
#
#Constraints:
#
#    nums1.length == m
#    nums2.length == n
#    0 <= m <= 1000
#    0 <= n <= 1000
#    1 <= m + n <= 2000
#    -106 <= nums1[i], nums2[i] <= 106
#
#Accepted
#2.2M
#Submissions
#5.7M
#Acceptance Rate
#38.1%
#

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #return Solution.linearMergeSolution(nums1, nums2)
        #return Solution.sublinearMedian(nums1, nums2)
        return Solution.sortSolution(nums1, nums2)

    def sublinearMedian(nums1, nums2):
        if len(nums1) == 0:
            return Solution.midPointWithGap(nums2, [])
        elif len(nums2) == 0:
            return Solution.midPointWithGap(nums1, [])

        if nums1[-1] < nums2[0]: # should be <=
            return Solution.midPointWithGap( nums1, nums2)

        if nums2[-1] < nums1[0]:
            return Solution.midPointWithGap(nums2, nums1)

        if nums1[0] < nums2[0]:
            return Solution.subLinearWithIntersect(nums1, nums2)

        return Solution.subLinearWithIntersect(nums2, nums1)

    # 1, 2, [4, 6, 8
    #          5, 7, 9], 10, 11, 12
    #
    # objective: limit linear merge to the overlapping reason between 4 .. 9
    #
    # for 5 -> find 4 in other array (just smaller than 4)
    # adjust counters to start merge from 4

    def subLinearWithIntersect(smallerFirst, largerFirst):

        lwIdx = Solution.findElemSmallerThan(largerFirst[0], smallerFirst, 0, len(smallerFirst)-1)
        return Solution.linearMergeSolution(smallerFirst, largerFirst, lwIdx)



    def findElemSmallerThan(value, array, low, high):
        if low > high:
            assert low == 0
            return low

        mid = (low + high) // 2

        if low < len(array)-1 and array[low] < value and array[low+1] >= value:
            return low

        if high < len(array)-1 and array[high] < value and array[high+1] >= value:
            return low

        if mid == 0 or mid == len(array)-1:
            return mid

        if array[mid] < value and array[mid+1] >= value:
            return mid

        if array[mid] >= value:
            return Solution.findElemSmallerThan(value, array, low, mid-1)
        return Solution.findElemSmallerThan(value, array, mid+1, high)



    def midPointWithGap(nums1, nums2):
        sum_len = len(nums1) + len(nums2)
        if sum_len % 2 == 1:
            mid_point = sum_len // 2
            return Solution.getAt(mid_point, nums1, nums2)

        return (Solution.getAt(sum_len // 2 - 1, nums1, nums2) + Solution.getAt(sum_len // 2, nums1, nums2)) / 2


    def getAt(idx, nums1, nums2):
        if idx < len(nums1):
            return nums1[idx]
        return nums2[idx - len(nums1)]


    def linearMergeSolution(nums1, nums2, nums1_offset = 0):

        sum_size = len(nums1) + len(nums2)
        mid_point = (sum_size // 2) + 1

        if mid_point < nums1_offset:
            prev_value = nums1[mid_point-1]
            cur_value = nums1[mid_point]
        else:
            nums1_pos = nums1_offset
            nums2_pos = 0
            count = nums1_offset

            cur_value = 0
            prev_value = 0

            if nums1_offset != 0:
                cur_value = nums1[nums1_offset-1]

            while count < mid_point:

                prev_value = cur_value
                if nums1_pos >= len(nums1):
                    cur_value = nums2[nums2_pos]
                    nums2_pos += 1
                elif nums2_pos >= len(nums2):
                    cur_value = nums1[nums1_pos]
                    nums1_pos += 1
                elif nums1[nums1_pos] < nums2[nums2_pos]:
                    cur_value = nums1[nums1_pos]
                    nums1_pos += 1
                else:
                    cur_value = nums2[nums2_pos]
                    nums2_pos += 1
                count += 1

        if sum_size % 2 == 1:
            return cur_value

        return (prev_value + cur_value) / 2


    def sortSolution(nums1, nums2):
        nums1.extend(nums2)
        nums1.sort()

        half = len(nums1) // 2

        if len(nums1) % 2 == 1:
            return nums1[ half ]
        return (nums1[ half ] + nums1[ half - 1 ]) / 2


