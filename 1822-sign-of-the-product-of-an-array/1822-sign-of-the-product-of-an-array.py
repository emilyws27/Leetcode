class Solution:
    def arraySign(self, nums: List[int]) -> int:
       
        
        prod = math.prod(nums)
        if prod > 0:
            return 1
        elif prod < 0:
            return -1
        else:
            return 0
        
        
            