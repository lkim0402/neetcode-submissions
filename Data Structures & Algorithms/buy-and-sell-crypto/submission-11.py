class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1: return 0
        maxP = 0
        l, r = 0, 1

        while (r < len(prices)):
            curP = prices[r] - prices[l]
            maxP = max(maxP, curP)
            if curP < 0:
                l = r
            r += 1
        return maxP
