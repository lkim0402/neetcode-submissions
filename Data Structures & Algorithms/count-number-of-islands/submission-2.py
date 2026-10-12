class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid) - 1, len(grid[0]) - 1
        island_num = 0
        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        def dfs(r, c):
            
            # OOB 
            if r < 0 or r > ROWS or c < 0 or c > COLS:
                return
            
            # visited
            if grid[r][c] == "0":
                return 
            
            # not visited and not OOB
            grid[r][c] = "0" # mark as visited
            
            for dr, dc in directions:
                new_r = r + dr
                new_c = c + dc
                dfs(new_r, new_c)

        # running the dfs for every coordinate
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    island_num += 1
                    dfs(i, j)   
        
        return island_num