class Solution:
    def twoSum(self, arr: List[int], target_sum: int) -> List[int]:
        seen = {}
        for index, val in enumerate(arr):
            remaining = target_sum - val
            if remaining in seen:
                return [seen[remaining], index]
            seen[val] = index
        return []