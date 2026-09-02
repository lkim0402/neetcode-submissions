class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        ROWS = len(grid)
        COLS = len(grid[0])

        def dfs(x,y):
            # base case - oob / its water
            if 0 > x or x >= ROWS or 0 > y or y >= COLS or grid[x][y] == "0":
                return
            
            # its land -> recurse
            grid[x][y] = "0"
            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)

        # lets try the dfs version!!!
        for x in range(ROWS):
            for y in range(COLS):
                # dfs
                if grid[x][y] == "1":
                    islands += 1
                    dfs(x,y)

        return islands