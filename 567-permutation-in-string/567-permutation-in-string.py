class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2)<len(s1):
            return False
        
        sorted_s1 = sorted(s1)
        window_size = len(sorted_s1)
        start=0
        end = start+window_size
        while end <= len(s2):
            if sorted(s2[start:end]) == sorted_s1:
                return True
            
            start += 1
            end += 1
        
        return False
        