class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # 1st binary search
        rowLen = len(matrix)
        colLen = len(matrix[0])

        top = 0
        bot = rowLen - 1

        while (top <= bot):
            mid = (top + bot) // 2
            
            if target > matrix[mid][-1]:
                top = mid + 1
            elif target < matrix[mid][0]:
                bot = mid - 1
            else:
                break
        
        if top > bot: 
            return False
        
        # 2nd binary search
        row = matrix[mid]
        l = 0
        r = len(row) - 1
        while(l <= r):
            mid =(l + r)//2
            cur = row[mid]

            if target == cur:
                return True
            elif target > cur:
                l = mid + 1
            else:
                r = mid - 1
    
        return False

