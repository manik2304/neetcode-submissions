class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        curr_profit = 0

        for price in prices:
            curr_profit = price - min_price
            max_profit = max(max_profit, curr_profit)
            min_price = min(min_price, price)

        return max_profit

