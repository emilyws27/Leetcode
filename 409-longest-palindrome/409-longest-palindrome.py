class Solution:
    def longestPalindrome(self, s: str) -> int:
        pairs = 0
        unpaired = set()
        
        for char in s:
            if char in unpaired:
                pairs += 1
                unpaired.remove(char)
            else:
                unpaired.add(char)
        if unpaired:
            return pairs * 2 + 1
      
        return pairs*2