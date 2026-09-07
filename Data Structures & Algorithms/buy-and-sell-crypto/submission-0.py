class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        max_profit = 0

        for i in range(1, len(prices)):
            if prices[i] - prices[l] > max_profit:
                max_profit = prices[i] - prices[l]
            
            if prices[i] < prices[l]:
                l = i
        return max_profit

        