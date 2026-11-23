class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        ROWS, COLS = len(image), len(image[0])
        org_color = image[sr][sc]
        if color == org_color: return image

        def dfs(r, c):
            # check OOB
            if (r < 0 or r >= ROWS or c < 0 or c >= COLS):
                return 

            cur = image[r][c]
            if cur == org_color:
                # change the color
                image[r][c] = color
                dfs(r + 1, c)
                dfs(r - 1, c)
                dfs(r, c + 1)
                dfs(r, c - 1)
        
        dfs(sr, sc)
        return image