# 930. Binary Subarrays With Sum
# Medium
#Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.
#
#A subarray is a contiguous part of the array.
#
# 
#
#Example 1:
#
#Input: nums = [1,0,1,0,1], goal = 2
#Output: 4
#Explanation: The 4 subarrays are bolded and underlined below:
#[1,0,1,0,1]
#[1,0,1,0,1]
#[1,0,1,0,1]
#[1,0,1,0,1]
#
#Example 2:
#
#Input: nums = [0,0,0,0,0], goal = 0
#Output: 15
#
# 
#
#Constraints:
#
#    1 <= nums.length <= 3 * 104
#    nums[i] is either 0 or 1.
#    0 <= goal <= nums.length
#


import bisect

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:        
        prefix_map = defaultdict(int)
        sm = ret = 0

        for n in nums:
            sm += n
        
            target = sm - goal            
            ret += prefix_map[target]

            prefix_map[sm] += 1

        ret += prefix_map[goal] 
        return ret




    def slowww(nums, gooal):
        prefix_map = defaultdict(list)

        sm = 0
        for idx in range(len(nums)):
            sm += nums[idx]
            prefix_map[sm].append(idx)

        for v in prefix_map.values():
            v.sort()
            
        ret = 0
        lk = prefix_map.get(goal)
        if lk is not None:
            ret += len(lk)

        #print(f"init ret {ret}")
        #print(prefix_map)

        for k, vec in prefix_map.items():
            target = k - goal 
            if k == target:
                ret += len(vec) * (len(vec)-1) // 2
                continue 

            other = prefix_map.get(target)
            if other is not None:
                #print(f"{k} vec {vec} target {target} other {other}")
                if max(vec) < max(other):    
                    big_v = other
                    small_v = vec
                else:
                    big_v = vec
                    small_v = other 

                #print(f"{big_v} {small_v}")

                for idxv in range(0, len(big_v)):
                    ridx = bisect.bisect_left(small_v, big_v[idxv])
                    if ridx != -1:
                        #print(f"{big_v} {big_v[idxv]} {small_v} {ridx}")
                        ret += ridx

        return ret        

        
