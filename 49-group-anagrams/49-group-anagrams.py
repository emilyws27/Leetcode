class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for word in strs:
            alpha = ''.join(sorted(word))
            
            if alpha in d:
                d[alpha].append(word)
            else:
                d[alpha] = []
                d[alpha].append(word)
        return list(d.values())