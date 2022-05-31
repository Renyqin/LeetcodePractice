class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum_buy = float('inf')
        max_gap = 0
        for price in prices:
            if price < minimum_buy:
                minimum_buy = price
            if price-minimum_buy > max_gap:
                max_gap = price-minimum_buy
        return max_gap
            