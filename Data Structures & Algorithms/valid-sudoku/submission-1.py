class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # each key value is a set
        rows = collections.defaultdict(set) # row num : { numbers in row }
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):

                num = board[r][c]

                if num == ".":
                    continue
                
                in_row = num in rows[r] 
                in_col = num in cols[c]
                in_square = num in squares[(r // 3, c // 3)]

                if ( in_row or in_col or in_square):
                    return False
                
                # adding to dicts
                rows[r].add(num)
                cols[c].add(num)
                squares[(r//3, c//3)].add(num)
        
        return True