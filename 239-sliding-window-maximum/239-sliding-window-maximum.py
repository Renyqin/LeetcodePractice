from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        ans = []
        for index, num in enumerate(nums):
            
            while q and nums[q[-1]] < num:
                q.pop()
            
            q.append(index)
            
            if q[0] == index-k:
                q.popleft()
                
            if index >= k-1:
                ans.append(nums[q[0]])
            
        
    
        return ans