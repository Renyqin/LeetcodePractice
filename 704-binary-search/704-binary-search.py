class Solution:
    # recursive way 
    """def recursive_search(self, low, high, nums, target):
        if high < low:
            return -1
        mid = low + int((high-low)//2)
        
        if target == nums[mid]:
            return mid
        
        elif target > nums[mid]:
            return self.recursive_search(mid+1, high, nums, target)
        elif target < nums[mid]:
            return self.recursive_search(low, mid-1, nums, target)
       
        
        
    def search(self, nums: List[int], target: int) -> int:
        return self.recursive_search(0, len(nums)-1, nums, target)"""
    
    
    # iteration way 
    
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1
        while high >= low:
            mid = low + int((high-low)//2)
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                low = mid + 1
            elif target < nums[mid]:
                high = mid - 1
                
        return -1