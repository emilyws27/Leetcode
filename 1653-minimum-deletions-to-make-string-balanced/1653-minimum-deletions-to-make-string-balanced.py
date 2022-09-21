class Solution:
    def minimumDeletions(self, s: str) -> int:
        stack = []
        res = 0
        
        for i in range(0 , len(s)):
            if s[i] == 'b':
                stack.append('b')
            else:
                if len(stack) == 0:
                    continue
                else:
                    stack.pop()
                    res += 1
        return res