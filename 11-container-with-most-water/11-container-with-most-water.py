class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        max_volume = 0
        while l<r:
            new_volume = min(height[r], height[l]) * (r-l)
            max_volume = max(max_volume, new_volume) 
            if height[l] >= height[r]:
                r-=1
            else:
                l+=1
        return max_volume