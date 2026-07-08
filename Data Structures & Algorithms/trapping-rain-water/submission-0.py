class Solution:
    def trap(self, height: List[int]) -> int:

        L = 0
        R = len(height) - 1
        maxL = height[L]
        maxR = height[R]
        water = 0

        while (L < R):
            if height[L] < height[R]:
                L += 1
                maxL = max(maxL, height[L])
                water += maxL - height[L]
            else:
                R -= 1
                maxR = max(maxR, height[R])
                water += maxR - height[R]

        return water
