class Solution:
    def romanToInt(self, s: str) -> int:
        romans = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        
        total = 0
        i = 0
        while i < len(s):
            # If this is the subtractive case.
            if i + 1 < len(s) and romans[s[i]] < romans[s[i + 1]]:
                total += romans[s[i + 1]] - romans[s[i]]
                i += 2
            # Else this is NOT the subtractive case.
            else:
                total += romans[s[i]]
                i += 1
        return total