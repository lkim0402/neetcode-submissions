class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()

        # iterating over rows
        for row in board:
            for num in row:
                if num == ".":
                    continue
                if num in seen:
                    return False
                seen.add(num)
            seen.clear()

        # iterating over cols
        for i in range(9):
            for j in range(9):
                num = board[j][i]
                if num == ".":
                    continue
                if num in seen:
                    return False
                seen.add(num)
            seen.clear()
        
        # iterating over boxes
        """
                0      1     2
             (0,1,2) (3,4,5) (6,7,8)
        0 (0,
           1,
           2)  
        1 (3,
           4,
           5)
        2 (6,
           7,            x
           8)
    
        """
        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square // 3) * 3 + i
                    col = (square % 3) * 3 + j

                    num = board[row][col]

                    if num == ".":
                        continue
                    if num in seen:
                        return False
                    seen.add(num)
        return True    

