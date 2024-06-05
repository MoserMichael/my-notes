# 347. Top K Frequent Elements
# Medium
#Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
#
#
#
#Example 1:
#
#Input: nums = [1,1,1,2,2,3], k = 2
#Output: [1,2]
#
#Example 2:
#
#Input: nums = [1], k = 1
#Output: [1]
#
#
#
#Constraints:
#
#    1 <= nums.length <= 105
#    -104 <= nums[i] <= 104
#    k is in the range [1, the number of unique elements in the array].
#    It is guaranteed that the answer is unique.
#
#
#
#Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
#

import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        num_count = Counter(nums)

        min_heap = []

        for key, val in num_count.items():
            if len(min_heap) < k:
                heapq.heappush(min_heap, (val, key) )
            else:
                if val > min_heap[0][0]:
                    heapq.heapreplace(min_heap, (val, key))

        return map(lambda v : v[1], min_heap)
