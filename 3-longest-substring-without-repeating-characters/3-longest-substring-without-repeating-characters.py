class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        w_start = 0
        max_length = 0
        hMap = {}
        for w_end in range(len(s)):
            start = s[w_end]
            if start in hMap:
                w_start = max(w_start, hMap[start]+1)
            hMap[start] = w_end;
            max_length = max(max_length, w_end - w_start + 1)
        return max_length