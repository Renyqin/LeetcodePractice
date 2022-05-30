import random
class Solution:
    # merge sort
    
    """def merge(self, l1, l2):
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
    """
    
    def partition(self, l, r, nums):
        pivot_index = random.randint(l,r-1)
        pivot = nums[pivot_index]
        
        nums[pivot_index], nums[l] = nums[l], nums[pivot_index]
        
        j = l
        for i in range(l+1, r):
            if nums[i] <= pivot:
                j += 1
                nums[j], nums[i] = nums[i], nums[j]

        nums[l], nums[j] = nums[j], nums[l]
        return j
    
    
    def quickSort(self, l, r, nums):
        if l >= r:
            return 
        
        mid = self.partition(l, r, nums)
        
        
        self.quickSort(l, mid, nums)
        self.quickSort(mid+1, r, nums)
    
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quickSort(0, len(nums), nums)
        return nums
    
    