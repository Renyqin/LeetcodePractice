class Solution:
    
    
    def indexToFlat(self, index, row_len):
        return index[0]*row_len + index[1]
    
    def flatToIndex(self, flat, row_len):
        return [flat//row_len, flat%row_len] 
    
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        row_len = len(matrix[0])
        left_flat = self.indexToFlat([0,0], row_len)
        right_flat = self.indexToFlat([len(matrix)-1, len(matrix[0])-1], row_len)
        
        while left_flat <= right_flat:
            mid_flat = (left_flat+right_flat) //2
            mid = self.flatToIndex(mid_flat, row_len)
            mid_value = matrix[mid[0]][mid[1]]
            if target == mid_value:
                return True
            elif target < mid_value:
                right_flat = mid_flat - 1
            else:
                left_flat = mid_flat + 1
    
        
        return False
    
