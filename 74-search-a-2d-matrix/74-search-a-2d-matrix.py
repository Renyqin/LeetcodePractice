class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flat_rows = []
        for row in matrix:
            flat_rows += row
        
        print(flat_rows)
        left = 0
        right = len(flat_rows)-1
        while right >= left:
            mid = left + (right-left)//2
            #print(mid)
            if target == flat_rows[mid]:
                return True
            elif target > flat_rows[mid]:
                left = mid + 1
            else:
                right = mid - 1
        
        return False
    