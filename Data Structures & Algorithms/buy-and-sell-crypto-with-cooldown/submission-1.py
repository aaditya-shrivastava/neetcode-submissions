class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # n = len(prices)
        # if n <= 1:
        #     return 0

        # buy = [0] * n
        # sell = [0] * n
        # cooldown = [0] * n

        # buy[0] = -prices[0]
        # sell[0] = 0
        # cooldown[0] = 0

        # for i in range(1, n):
        #     buy[i] = max(buy[i-1], cooldown[i-1] - prices[i])
        #     sell[i] = max(sell[i-1], buy[i-1] + prices[i])
        #     cooldown[i] = max(cooldown[i-1], sell[i-1])

        # return max(sell[n-1], cooldown[n-1])

        dp = {}
        def dfs(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying) in dp:
                return dp[(i,buying)]

            cooldown = dfs(i+1, buying)
            if buying:
                buy = dfs(i+1, not buying) - prices[i]
                dp[(i, buying)] = max(buy, cooldown)
            else:
                sell = dfs(i+2, not buying) + prices[i]
                dp[(i, buying)] = max(sell, cooldown)
            return dp[(i,buying)]
        return dfs(0,True)










