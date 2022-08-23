class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magNew = magazine
        for letter in ransomNote:
            if letter in magNew:
                idx = magNew.index(letter)
                magNew = magNew[:idx]+magNew[idx+1:]
                continue
            else:
                return False
        return True
                