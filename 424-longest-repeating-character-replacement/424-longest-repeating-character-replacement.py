class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        w_start, max_len, max_repeat_count = 0,0,0
        frequency_map = {}
        for w_end in range(len(s)):
            right_char = s[w_end];
            if right_char not in frequency_map:
                frequency_map[right_char] = 0;
            frequency_map[right_char] += 1
            
            max_repeat_count = max(max_repeat_count, frequency_map[right_char])
            
            if(w_end - w_start + 1 - max_repeat_count > k):
                left_char = s[w_start]
                frequency_map[left_char] -= 1
                w_start += 1
            max_len = max(max_len, w_end - w_start + 1)
        return max_len