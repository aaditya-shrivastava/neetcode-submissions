class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total_sum = sum(nums)
        if total_sum < abs(target) or (total_sum + target) % 2 == 1:
            return 0
        s = (total_sum + target) // 2
        if s < 0:
            return 0
        dp = [0] * (s + 1)
        dp[0] = 1
        for num in nums:
            for i in range(s, num - 1, -1):
                dp[i] += dp[i - num]
        return dp[s]