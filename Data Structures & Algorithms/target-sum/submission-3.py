class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # total_sum = sum(nums)
        # if total_sum < abs(target) or (total_sum + target) % 2 == 1:
        #     return 0
        # s = (total_sum + target) // 2
        # if s < 0:
        #     return 0
        # dp = [0] * (s + 1)
        # dp[0] = 1
        # for num in nums:
        #     for i in range(s, num - 1, -1):
        #         dp[i] += dp[i - num]
        # return dp[s]


        dp = {}
        def backtrack(i, total):
            if i == len(nums):
                return 1 if total == target else 0
            if (i, total) in dp:
                return dp[(i,total)]
            dp[(i, total)] = backtrack(i + 1,total+nums[i]) + backtrack(i + 1,total - nums[i])
            return dp[(i,total)]
        return backtrack(0,0)




