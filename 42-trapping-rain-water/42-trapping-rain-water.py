from collections import deque

class Solution:
    def trap(self, height: List[int]) -> int:
        q = deque()
        i = 1
        ans = 0
        q.append(0)
        while i < len(height):
            if not q:
                q.append(i)
            elif height[i] < height[i-1]:
                q.append(i)
            else:
                while q and height[i] >= height[q[-1]]:
                    #print(q)
                    pop_value = q.pop()
                    if q:
                        ans += (min(height[q[-1]], height[i])-height[pop_value]) * (i - q[-1]-1)
                        #print(ans)
                q.append(i)
            i += 1
        
        
        return ans