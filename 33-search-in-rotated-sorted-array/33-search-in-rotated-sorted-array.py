class Solution:
    
    def binary_search(self, nums: List[int], target: int) -> int:
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
    
    def search(self, nums: List[int], target: int) -> int:
        
        left = 0
        right = len(nums) -1
        
        while left <= right:
            mid = left + (right-left)//2
            if target == nums[mid]:
                return mid
            
            if nums[left] <= nums[mid]:
                if target < nums[mid] and target >= nums[left]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if target > nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return -1
            
            
             
            
        