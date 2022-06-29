class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
#         w_start = 0;
#         max_length = 0;
#         char_freq = {}
        
#         for w_end in range(len(fruits)):
#             end_char = fruits[w_end]
#             if end_char not in char_freq:
#                 char_freq[end_char] = 0;
#             char_freq[end_char] += 1;
#             while len(char_freq) > 2:
#                 char_start = fruits[w_start]
#                 char_freq[char_start] -= 1;
#                 if char_freq[char_start] == 0:
#                     del char_freq[char_start]
#             max_length = max(max_length, w_end - w_start +1)
#         return max_length
        window_start = 0
        max_length = 0
        fruit_frequency = {}

        # try to extend the range [window_start, window_end]
        for window_end in range(len(fruits)):
            right_fruit = fruits[window_end]
            if right_fruit not in fruit_frequency:
                fruit_frequency[right_fruit] = 0
            fruit_frequency[right_fruit] += 1

        # shrink the sliding window, until we are left with '2' fruits in the fruit 
        # frequency dictionary
            while len(fruit_frequency) > 2:
                left_fruit = fruits[window_start]
                fruit_frequency[left_fruit] -= 1
                if fruit_frequency[left_fruit] == 0:
                    del fruit_frequency[left_fruit]
                window_start += 1  # shrink the window
            max_length = max(max_length, window_end-window_start + 1)
        return max_length