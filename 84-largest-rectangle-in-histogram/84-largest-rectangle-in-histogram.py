class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        dummy = (0,-1)
        stack =[]
        stack.append(dummy)
        max_rectangle = 0
        for index, h in enumerate(heights):
            while stack and h<stack[-1][0]:
                ele = stack.pop()
                temp = ele[0] * (index-stack[-1][1]-1)
                max_rectangle = max(max_rectangle, temp)
            
                
            stack.append((h,index))

        if len(stack)>1: 
            i=1
            while i<len(stack):
                temp = stack[i][0]*(len(heights)-stack[i-1][1]-1)
                max_rectangle = max(max_rectangle, temp)
                i+=1

            return max_rectangle
            
        
        