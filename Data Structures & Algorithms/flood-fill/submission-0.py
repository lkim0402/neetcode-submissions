class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        original_color = image[sr][sc]
        if color == original_color: return image
        
        ROWS, COLS = len(image), len(image[0])

        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        
        def dfs(r,c):
            # check OOB
            if 0 > r or r >= ROWS or 0 > c or c >= COLS:
                return
            
            # check same color
            if image[r][c] != original_color:
                return
            
            # else, modify color
            image[r][c] = color

            for d in directions:
                new_x = r + d[0]
                new_y = c + d[1]
                # dfs on the 4 neighbors
                dfs(new_x, new_y)

        dfs(sr, sc)
        
        return image