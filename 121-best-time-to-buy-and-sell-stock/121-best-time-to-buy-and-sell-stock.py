class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum_buy = float('inf')
        max_gap = 0
        for price in prices:
            minimum_buy = min(price, minimum_buy)
            max_gap = max(price-minimum_buy, max_gap)
        return max_gap
            