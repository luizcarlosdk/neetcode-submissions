class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i,j = 0,0
        max_profit = -1
        for i in range(len(prices)):
            for j in range(i, len(prices)):

                current_profit = prices[j] - prices[i]
                max_profit = max(current_profit, max_profit)
        
        return max_profit
