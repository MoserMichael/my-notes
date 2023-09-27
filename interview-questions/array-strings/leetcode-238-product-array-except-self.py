class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prodAll = reduce((lambda x, y: x * y), nums)
        if prodAll != 0:
            return map(lambda x : int(prodAll / x), nums)

        res = []
        
        for i in range(0, len(nums)):
            prod = 1
            for pos, val in enumerate(nums):
                if pos != i:
                    prod *= val                    
            res.append(prod)    
        
        return res

        
