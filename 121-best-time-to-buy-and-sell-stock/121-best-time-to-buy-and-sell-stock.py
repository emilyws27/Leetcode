
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_profit = float('inf')
    
        for i in range(len(prices)):
            if prices[i] < min_profit:
                min_profit = prices[i]
            elif prices[i] - min_profit > max_profit:
                max_profit = prices[i] - min_profit
        return max_profit