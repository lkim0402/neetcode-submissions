class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        """
        1. mark where the trasures are at in q
        2. loop thru the treasure q, expand
            - when u find an inf, replace it with the distance so far
        """

        ROWS = len(grid)
        COLS = len(grid[0])
        INF = 2147483647
        q = deque()
        visited = set()

        for x in range(ROWS):
            for y in range(COLS):
                if grid[x][y] == 0: # marking treasures
                    q.append([x,y])
                    visited.add((x,y))

        def addRoom(x,y):
            if (x < 0 or x >= ROWS or 
                y < 0 or y >= COLS or 
                grid[x][y] != INF or
                (x,y) in visited):
                return
            visited.add((x,y))
            q.append([x,y])


        dist = 0
        while q:
            # freezing per batch
            for i in range(len(q)):
                x,y = q.popleft()
                # update to dist
                grid[x][y] = dist
                # add to queue our next batch
                addRoom(x + 1, y)
                addRoom(x - 1, y)
                addRoom(x, y + 1)
                addRoom(x, y - 1)

            # increment dist
            dist += 1

            
                
