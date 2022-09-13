class Solution:
    def minSteps(self, s: str, t: str) -> int:
        d = {k:s.count(k) for k in set(s)}
        for letter in t:
            if letter in d and d[letter]>0:
                d[letter] -= 1
        return sum(d.values())
        
        