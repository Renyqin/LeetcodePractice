class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for prth in s:
            if len(stack) > 0:
                if (prth == ")" and stack[-1] == "(") or\
                    (prth == "]" and stack[-1] == "[") or\
                    (prth == "}" and stack[-1] == "{"):
                        stack.pop()
                        
                else:
                    stack.append(prth)
            else:
                stack.append(prth)
                
        return len(stack) == 0
    
        
        
