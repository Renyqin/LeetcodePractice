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
        
        i = 1 
        rot_end = rot_start = -1
        
        while i<len(nums):
            if nums[i]<nums[i-1]:
                rot_end = i-1
                rot_start = i
            
            i+=1
        #print(rot_start)
            
        if rot_end == -1:
            return self.binary_search(nums, target)
        
        else:
            first_search = self.binary_search(nums[:rot_start], target)
            print()
            if first_search != -1:
                return first_search
            else:
                second_search =  self.binary_search(nums[rot_start:], target)
                if second_search != -1:
                    return rot_start + second_search
                else:
                    return -1
            
             
            
        