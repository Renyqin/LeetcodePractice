class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        dp = [0]*(amount+1)
        coins = set(coins)
        for i in range(amount+1):
            if i in coins:
                dp[i] = 1
            else:
                minimum = float("inf")
                for coin in coins:
                    if i - coin > 0:
                        minimum = min(dp[i-coin], minimum)
                dp[i] = minimum + 1
        
        if dp[-1] == float("inf"):
            return -1
        else:
            return dp[-1]