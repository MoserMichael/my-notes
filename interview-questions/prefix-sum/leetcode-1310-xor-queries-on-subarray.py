# 1310. XOR Queries of a Subarray
# Medium
#
#    You are given an array arr of positive integers. You are also given the array queries where queries[i] = [lefti, righti].
#
#    For each query i compute the XOR of elements from lefti to righti (that is, arr[lefti] XOR arr[lefti + 1] XOR ... XOR arr[righti] ).
#
#    Return an array answer where answer[i] is the answer to the ith query.
#
#     
#
#    Example 1:
#
#    Input: arr = [1,3,4,8], queries = [[0,1],[1,2],[0,3],[3,3]]
#    Output: [2,7,14,8] 
#    Explanation: 
#    The binary representation of the elements in the array are:
#    1 = 0001 
#    3 = 0011 
#    4 = 0100 
#    8 = 1000 
#    The XOR values for queries are:
#    [0,1] = 1 xor 3 = 2 
#    [1,2] = 3 xor 4 = 7 
#    [0,3] = 1 xor 3 xor 4 xor 8 = 14 
#    [3,3] = 8
#
#    Example 2:
#
#    Input: arr = [4,8,2,10], queries = [[2,3],[1,3],[0,0],[0,3]]
#    Output: [8,0,4,4]
#
#     
#
#    Constraints:
#
#        1 <= arr.length, queries.length <= 3 * 104
#        1 <= arr[i] <= 109
#        queries[i].length == 2
#        0 <= lefti <= righti < arr.length
#
#    
#


import bisect
import collections

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        return Solution.usePrefix(arr, queries)
        #return Solution.useCache(arr, queries)

    
    def usePrefix(arr, queries):
        ret = [0] * len(queries)
        prefix = [arr[0]] * len(arr)

        r = arr[0]
        for idx in range(1,len(arr)):
            r ^= arr[idx]
            prefix[idx] = r
        
        for qidx,q in enumerate(queries):
            if q[0] != 0:
                ret[qidx] = prefix[q[1]] ^ prefix[q[0]-1]
            else:
                ret[qidx] = prefix[q[1]]
        
        return ret



    def useCache(arr, queries):
        cache = collections.defaultdict(list)
        ret = [0] * len(queries)
        
        for qidx,q in enumerate(queries):
            
            #print(f"? {qidx} - {q}")
            idx=q[0]
            to_idx = q[1]
            
            first=True
            r=arr[idx]
            
            while idx <= to_idx:

                cfound = False
                if idx in cache:
                    #print(f"cache: {idx} -> {cache} to_idx {to_idx}")
                    centry=cache[idx]
                    fidx=bisect.bisect_left(centry, to_idx, key=lambda entry : entry[0])
                    if fidx > 0:
                        cfound = True
                        entry = centry[fidx-1]
                    elif fidx == 0 and len(centry) != 0 and centry[0][0]<=to_idx:
                        cfound = True
                        entry = centry[0]
                    
                    if cfound:
                        #print(f"found: {idx} -> {entry}")

                        idx = entry[0]+1
                        rangeRes=entry[1]
                else:
                    centry = []

                if not cfound:
                    rangeRes = arr[idx]
                    for idx2 in range(idx+1,to_idx+1):
                        rangeRes ^= arr[idx2]
                    
  
                    bisect.insort_left(centry, (to_idx, rangeRes), key=lambda entry: entry[0])
                    cache[idx] = centry
                    #print(f"cache-add {idx} -> {centry}")

                    idx=to_idx+1


                if first:
                    r = rangeRes
                    first = False
                else:
                    r ^= rangeRes

            ret[qidx] = r
        return ret

    def naive(arr: List[int], queries: List[List[int]]):
        ret = [0] * len(queries)
        for idx,q in enumerate(queries):
            r = arr[q[0]]
            for idx2 in range(q[0]+1,q[1]+1):
                r = r ^ arr[idx2]
            ret[idx] = r
        return ret

        
