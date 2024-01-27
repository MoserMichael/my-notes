# 40. Combination Sum II
# Medium
#    Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.
#
#    Each number in candidates may only be used once in the combination.
#
#    Note: The solution set must not contain duplicate combinations.
#
#     
#
#    Example 1:
#
#    Input: candidates = [10,1,2,7,6,1,5], target = 8
#    Output: 
#    [
#    [1,1,6],
#    [1,2,5],
#    [1,7],
#    [2,6]
#    ]
#
#    Example 2:
#
#    Input: candidates = [2,5,2,1,2], target = 5
#    Output: 
#    [
#    [1,2,2],
#    [5]
#    ]
#
#     
#
#    Constraints:
#
#        1 <= candidates.length <= 100
#        1 <= candidates[i] <= 50
#        1 <= target <= 30
#
#


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        return self.faster(candidates, target)
        #return self.slow(candidates, target)


    def faster(self, candidates, target):
        candidates.sort()
        self.ret = []
        self.candidates = candidates

        self.rec2(0, target, [])
        return self.ret

    def rec2(self, pos, target, num_so_far):
        
        if target == 0:
            to_add = num_so_far.copy()
            self.ret.append( to_add )
            return

        if pos >= len(self.candidates):
            return

        if self.candidates[pos] <= target:
            num_so_far.append( self.candidates[pos] )
            self.rec2( pos+1, target-self.candidates[pos], num_so_far)
            num_so_far.pop()
    
        diff = 1
        while pos + diff < len(self.candidates) and self.candidates[pos+diff] == self.candidates[pos]:
            diff += 1
        self.rec2( pos+diff, target, num_so_far)


    def slow(self, candidates, target):
        self.ret = set()
        self.candidates = candidates

        self.rec(0, target, [])

        ret_list = []
        for e in self.ret:
            ret_list.append( list(e) )
        return ret_list

    def rec(self, pos, target, num_so_far):
        
        if target == 0:
            to_add = num_so_far.copy()
            to_add.sort()
            self.ret.add( tuple( to_add ) )
            return

        if pos >= len(self.candidates):
            return

        if self.candidates[pos] <= target:
            num_so_far.append( self.candidates[pos] )
            self.rec( pos+1, target-self.candidates[pos], num_so_far)
            num_so_far.pop()
    
        diff = 1
        while pos + diff < len(self.candidates) and self.candidates[pos+diff] == self.candidates[pos]:
            diff += 1
        self.rec( pos+diff, target, num_so_far)

        
    
