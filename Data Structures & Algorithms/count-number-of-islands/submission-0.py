class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        islands = 0
        q = deque() 
        ROWS = len(grid)
        COLS = len(grid[0])

        for i in range(ROWS):
            for j in range(COLS):
                # find the entire connected land
                if grid[i][j] == "1":
                    islands += 1
                    q.append((i,j))
                    grid[i][j] == "0" # marking it 
                    # up, down, right, left
                    directions = [(0,1), (0,-1), (1,0), (-1,0)]
                    while q:
                        x,y = q.popleft()
                        for d in directions:
                            dx = d[0] + x
                            dy = d[1] + y
                            if (0 <= dx < ROWS) and (0 <= dy < COLS) and (grid[dx][dy] == "1"):
                                grid[dx][dy] = "0" # mark it
                                q.append((dx, dy))
        
        return islands
