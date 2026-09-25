class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_prof = 0
        buy = prices[0]
        for price in prices:
            max_prof = max(max_prof, price - buy)
            if price < buy:
                buy = price
        return max_prof