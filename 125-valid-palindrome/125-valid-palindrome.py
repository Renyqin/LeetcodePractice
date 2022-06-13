class Solution:
    """def isPalindrome(self, s: str) -> bool:
        cleaned_s = []
        for l in s: 
            if l.isalpha() or l.isdigit():
                cleaned_s.append(l.lower())
        return cleaned_s[::-1] == cleaned_s
    """
    
    def isPalindrome(self, s: str) -> bool:
        cleaned_s = []
        for l in s:
            if l.isalpha() or l.isdigit():
                cleaned_s.append(l.lower())
        
        i = 0
        j = len(cleaned_s)-1
        while i<j:
            if cleaned_s[i] != cleaned_s[j]:
                return False
            
            i += 1
            j -= 1
        
        return True
            
            