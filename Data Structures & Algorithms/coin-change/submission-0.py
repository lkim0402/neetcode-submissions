class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        index = amount
        how many coins for amount = [0,_,_]
        amount                    =  0 1 2
        """
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                curAmount = a - c
                if curAmount >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])
        
        return dp[amount] if dp[amount] != amount + 1 else - 1