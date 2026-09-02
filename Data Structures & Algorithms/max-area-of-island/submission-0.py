class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        ROWS = len(grid)
        COLS = len(grid[0])

        # get the area
        def dfs(x,y):
            # base case - oob or it's water
            if x < 0 or x >= ROWS or y < 0 or y >= COLS or grid[x][y] == 0:
                return 0 
            
            # it's land!
            grid[x][y] = 0
            right = dfs(x + 1, y)
            left = dfs(x - 1, y)
            up = dfs(x, y + 1)
            down = dfs(x, y - 1)

            return 1 + right + left + up + down
        
        for x in range(ROWS):
            for y in range(COLS):
                if grid[x][y] == 1:
                    area = dfs(x,y)
                    maxArea = max(area, maxArea)
        
        return maxArea