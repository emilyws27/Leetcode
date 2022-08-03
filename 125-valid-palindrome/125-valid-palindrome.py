class Solution:
    def isPalindrome(self, s: str) -> bool:
        inwards, outwards = 0, len(s)- 1
        
        while inwards < outwards:
            while inwards < outwards and not s[inwards].isalnum():
                inwards += 1
            while inwards < outwards and not s[outwards].isalnum():
                outwards -= 1
            if s[inwards].lower() != s[outwards].lower():
                return False
            inwards += 1
            outwards -= 1
        return True