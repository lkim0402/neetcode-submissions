class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if len(prices) == 1: return 0

        profit = 0
        low = 0
        high = 1

        # 7 1 5 3 6 4
        # l h       
        while high < len(prices):
            if prices[low] > prices[high]:
                low += 1
            else:
                profit = max(profit, prices[high] - prices[low])
                high += 1
        
        return profit
            



        
        