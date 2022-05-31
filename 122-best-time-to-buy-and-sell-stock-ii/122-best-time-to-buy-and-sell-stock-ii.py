class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prices.append(0)
        buy = prices[0]
        sell = 0
        # gap = sell-buy
        ans = 0
        i = 0
        j = i+1
        while j < len(prices):
            if prices[j] < prices[i]:
                sell = prices[i]
                ans += sell - buy
                buy = prices[j]
            i += 1
            j += 1
                
        return ans
            
        