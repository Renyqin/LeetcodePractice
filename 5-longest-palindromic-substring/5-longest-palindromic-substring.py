class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <2:
            return s
        
        dp = [[None] * len(s) for i in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True
            
        for right in range(len(s)):
            for left in range(right):
                #print(str(j) + " " + str(i))
                dp[left][right] = (s[left] == s[right]) and (right-left < 3 or dp[left+1][right-1])
        
        
        #print(dp)
        
      
        max_len = 0
        max_string = s[0]
        for right in range(len(s)-1, -1, -1):
            for left in range(right-1, -1, -1):
                if dp[left][right] and (right-left + 1) > max_len:
                    max_len = right-left + 1
                    max_string = s[left:right+1]
            
        
            
        return max_string
        