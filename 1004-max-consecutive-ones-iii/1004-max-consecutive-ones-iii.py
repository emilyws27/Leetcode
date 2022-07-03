class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        w_start, max_len, max_ones = 0,0,0
        for w_end in range(len(nums)):
            if nums[w_end] == 1:
                max_ones += 1
            if (w_end - w_start + 1 - max_ones) > k:
                if nums[w_start] == 1:
                    max_ones -= 1
                w_start += 1;
            max_len = max(max_len, w_end - w_start + 1)
        return max_len
        # window_start, max_length, max_ones_count = 0, 0, 0
        # for window_end in range(len(nums)):
        #     if nums[window_end] == 1:
        #         max_ones_count += 1
        #     if (window_end - window_start + 1 - max_ones_count) > k:
        #         if nums[window_start] == 1:
        #             max_ones_count -= 1
        #         window_start += 1
        #     max_length = max(max_length, window_end - window_start + 1)
        # return max_length
