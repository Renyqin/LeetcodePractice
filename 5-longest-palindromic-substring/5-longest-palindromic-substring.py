class Solution:
    
    def expandFromCenter(self, s, longest, left, right, count, l_string):
        while s[left] == s[right]:
            count += 2
                
            if count > longest:
                l_string = s[left:right+1]
                longest = count
                    
            left -= 1
            right += 1
            if left < 0 or right >= len(s):
                break
        return longest, l_string
    
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        longest = 0
        l_string = s[0]
    
        
        for i in range(len(s)-1):
                
            even_len, even_string = self.expandFromCenter(s, longest, i, i+1, 0,l_string)
            if even_len > longest:
                longest = even_len
                l_string = even_string
                
            if i >0:
                odd_len, odd_string = self.expandFromCenter(s, longest, i-1, i+1, 1,l_string)
                if odd_len > longest:
                    l_string = odd_string
                    longest = odd_len
            
                
        
                    
                
        return l_string
                