class Solution:
    # merge sort
    
    def merge(self, l1, l2):
        new_array = []
        i = 0
        j = 0
        
        while i < len(l1) or j < len(l2):
            if l1[i] < l2[j]:
                new_array.append(l1[i])
                i+=1
            else:
                new_array.append(l2[j])
                j+=1
        return new_array
                
    def merge_sort(self, nums):
        n = len(nums)
        if n == 1:
            return nums
        mid = n//2
        l1 = self.merge_sort(nums[:mid])
        l2 = self.merge_sort(nums[mid:])
        new_array = merge(l1, l2)
        
        return new_array
    
    def sortArray(self, nums: List[int]) -> List[int]:
        
        return self.merge_sort(nums)
        