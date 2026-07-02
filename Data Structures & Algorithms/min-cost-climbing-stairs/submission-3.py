class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # n = len(cost)
        # if n == 0:
        #     return 0
        # if n == 1:
        #     return cost[0]
        # dp = [0] * (n + 1)
        # dp[0] = cost[0]
        # dp[1] = cost[1]
        # for i in range(2, n):
        #     dp[i] = cost[i] + min(dp[i-1], dp[i-2])
        # return min(dp[n-1], dp[n-2])
        cost.append(0)
        for i in range(len(cost)-3, -1,-1):
            cost[i] += min(cost[i+1],cost[i+2])
        return min(cost[0],cost[1])