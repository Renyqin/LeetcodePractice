class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        if len(grid) <1 or len(grid[0])<1:
            return 0
        
        #left = -1
        #up = -1
        #right = 1
        #down = 1
        
        perimeter = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    if i - 1 < 0 or grid[i-1][j]==0:
                        perimeter += 1
                    else:
                        #if grid[i-1][j] == 1:
                        pass
                    if i+1 > len(grid)-1 or grid[i+1][j]==0:
                        perimeter += 1
                    else:
                        #if grid[i+1][j] == 1:
                        pass
                    if j-1 <0 or grid[i][j-1] == 0:
                        perimeter += 1
                    else:
                        pass
                    if j+1 > len(grid[0])-1 or grid[i][j+1]==0:
                        perimeter += 1
                    else:
                        pass
                #print("i: " + str(i) + "j:" + str(j))
                #print(perimeter)
                    
        return perimeter
                    
                        