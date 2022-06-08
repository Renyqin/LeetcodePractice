class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_s = []
        for l in s: 
            if l.isalpha() or l.isdigit():
                cleaned_s.append(l.lower())
        return cleaned_s[::-1] == cleaned_s
            
            