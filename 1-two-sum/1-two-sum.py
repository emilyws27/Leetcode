class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for index, num in enumerate(nums):
            sum = target - num
            if sum in dict:
                return [nums.index(sum), index]
            else:
                dict[num] = True
        return []