class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        1. pre work
            - mark coordinates of rotten fruits
            - count total number of fruits
        2. loop per rotten fruits - bfs
            - mark the neighbors as rotten
            - repeat with the neighbors, time += 1
        """
        ROWS = len(grid)
        COLS = len(grid[0])
        time = 0
        fresh = 0
        rotten = 0

        # pre work
        q = deque()  # holds the rotten
        for x in range(ROWS):
            for y in range(COLS):
                if grid[x][y] == 2: # rotten
                    q.append([x,y])
                if grid[x][y] == 1: # not rotten
                    fresh += 1

        # loop
        dirs = [(0,1), (0, -1), (1,0), (-1,0)]
        while q and fresh:
            # frozen for the current wave (1 minute)
            for i in range(len(q)):
                x,y = q.popleft()
                # mark as empty
                for d in dirs:
                    dx = x + d[0]
                    dy = y + d[1]
                    # if in bounds and is fresh, add to q to make it rotten
                    if 0 <= dx < ROWS and 0 <= dy < COLS and grid[dx][dy] == 1:
                        grid[dx][dy] = 2 # rot immediately
                        q.append([dx, dy])

                        fresh -= 1
            time += 1
        
        return time if fresh == 0 else -1


