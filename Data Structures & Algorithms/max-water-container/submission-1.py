class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        get initial area (l, r pointer)
        move the shorter one
        """

        l = 0
        r = len(heights) - 1
        width = len(heights) - 1
        maxArea = 0

        while (l < r):
            left = heights[l]
            right = heights[r]
            smaller = min(left, right)
            area = smaller * width
            maxArea = max(area, maxArea) # storing the maximum area

            width -= 1
            if left < right:
                l += 1
            else:
                r -= 1
        
        return maxArea