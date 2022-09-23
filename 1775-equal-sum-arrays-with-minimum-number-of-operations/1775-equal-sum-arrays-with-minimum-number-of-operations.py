class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        sum1, sum2 = sum(nums1), sum(nums2)
        diff = abs(sum1-sum2)
        if diff == 0:
            return 0
        minOps = 0
        larger = nums1 if sum1 > sum2 else nums2
        smaller = nums2 if sum1 > sum2 else nums1
        heap = [(6-val)*-1 for val in smaller] + [(val-1)*-1 for val in larger]
        heapq.heapify(heap)
        while heap:
            val = heapq.heappop(heap)*-1
            diff-=val
            minOps+=1
            if diff <= 0:
                return minOps
        return -1    
        
# There will be a difference (diff) between the sum of nums1 and the sum of nums2
# To make the diff converges to 0 the fastest way, we want to make
# The list with larger sum, become smaller
# The list with smaller sum, become larger
# We define effort as the absolute difference between the new value & the original value
# In each turn, whoever makes the greater effort will get picked (use heap for the help)
# Above is the idea for the first while loop
# If there are nums1 or nums2 left over, use them up until the difference is less than or equal to 0
# Second & third while loop
# Return ans only if diff is less than or equal to 0, otherwise return -1 as there is no way to make diff to 0