class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        start = 0
        end = 3
        ans = 0
        while end <= len(s):
            sub = s[start:end]
            if len(set(sub)) == 3:
                ans += 1
            
            start += 1
            end += 1
        
        return ans