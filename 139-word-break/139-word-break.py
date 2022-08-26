class Solution:
    
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                if dp[i] and (s[i:j] in wordDict):
                    dp[j] = True
        
        #print(dp)
        
        return dp[-1]