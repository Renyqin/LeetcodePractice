class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        ana_dict = {}
        for l in s:
            if l in ana_dict:
                ana_dict[l] += 1
            else:
                ana_dict[l] = 1
        
        for j in t:
            
            if j in ana_dict:
                if ana_dict[j] < 1:
                    return False
                ana_dict[j] -= 1
            
            else:
                 return False
                
        return True
            
                
            