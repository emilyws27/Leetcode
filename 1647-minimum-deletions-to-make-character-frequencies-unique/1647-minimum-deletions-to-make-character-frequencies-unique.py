class Solution:
    def minDeletions(self, s: str) -> int:
        count = Counter(s)
        seen = set()
        
        number_deletions = 0
        for value in count.values():
            while value in seen and value > 0:
                value -= 1
                number_deletions += 1
            seen.add(value)
        return number_deletions
        
        