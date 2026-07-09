class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[-1] * n for _ in range(n)]
        def dfs(l, r):
            if l > r:
                return 0
            if dp[l][r] != -1:
                return dp[l][r]
            best = 0
            left = nums[l - 1]
            right = nums[r + 1]
            for i in range(l, r + 1):
                best = max(
                    best,
                    left * nums[i] * right +
                    dfs(l, i - 1) +
                    dfs(i + 1, r)
                )
            dp[l][r] = best
            return best
        return dfs(1, n - 2)