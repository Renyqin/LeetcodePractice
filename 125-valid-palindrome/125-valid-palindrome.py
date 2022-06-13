class Solution:
    """def isPalindrome(self, s: str) -> bool:
        cleaned_s = []
        for l in s: 
            if l.isalpha() or l.isdigit():
                cleaned_s.append(l.lower())
        return cleaned_s[::-1] == cleaned_s
    """
    
    def isPalindrome(self, s: str) -> bool:
        
        i = 0
        j = len(s)-1
        while i<j:
            
            if not (s[i].isalpha() or s[i].isdigit()):
                i+=1
                continue
            elif not (s[j].isalpha() or s[j].isdigit()):
                j-=1
                continue
                
            elif s[i].lower() != s[j].lower():
                return False
            

            i += 1
            j -= 1

        return True
            
            