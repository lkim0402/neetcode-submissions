class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        """
        loop thorugh all numbers. 
            if num == "1"
                do dfs()
        
        void dfs(r, c)
        """

        ROWS, COLS = len(grid), len(grid[0])
        islands = 0

        def dfs(r, c):
            # check OOB
            if r >= ROWS or r < 0 or c >= COLS or c < 0:
                return
            
            # check if 0
            if grid[r][c] == "0":
                return 
            
            # turn current coord to "0"
            grid[r][c] = "0"

            # dfs on the other directions
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    # do dfs search
                    dfs(r, c)
                    islands += 1

        return islands