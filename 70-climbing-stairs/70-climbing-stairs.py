class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return n
        
        first = 1
        second = 1
        for i in range(n-1):
            third = first + second
            first = second
            second = third
        return second