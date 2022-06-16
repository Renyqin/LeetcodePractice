class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 1:
            return 0
        start = 0
        end = start+1
        sub = set(s[start])
        max_len = 0

        while end < len(s):

            if s[end] in sub:
                max_len = max(max_len, len(sub))
                start +=1
                sub = set(s[start])
                
                end = start +1
            else:
                sub.add(s[end])
                end += 1
        
        max_len = max(max_len, len(sub))
    
        return max_len
            