class Solution:
    def minMoves(self, nums: List[int]) -> int:
        min_num = min(nums)
        lst = []
        for num in nums:
            lst.append(num-min_num)
        return sum(lst)