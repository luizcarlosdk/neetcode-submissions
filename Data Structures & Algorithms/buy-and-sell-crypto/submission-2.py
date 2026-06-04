class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 0
        minimum = prices[0]
        max_profit = 0

        while r < len(prices):
            profit = prices[r] - prices[l]
            max_profit = max(profit, max_profit)
            if prices[r] < minimum:
                l = r
                minimum = prices[l]
            r += 1
        
        return max_profit

# 7 1 5 3 6 4
#   l
#       r
# min 1
# profit 4

