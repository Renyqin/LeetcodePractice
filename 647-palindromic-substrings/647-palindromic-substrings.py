class Solution:
     
    def countSubstrings(self, s: str) -> int:
        dp = [[None]*len(s) for i in range(len(s))]
        
        #for i in range(len(dp)):
        #    dp[i][i] = True
            
        count = 0
        for right in range(len(dp)):
            for left in range(right+1):  
                dp[left][right] = (s[left] == s[right]) and (right-left < 2 or dp[left+1][right-1]) 
                if dp[left][right]:
                    count+=1
        
        
        #print(dp)
        
        return count
        