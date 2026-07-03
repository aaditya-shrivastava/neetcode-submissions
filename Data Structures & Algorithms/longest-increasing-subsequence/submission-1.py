class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ans = [1] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    ans[i] = max(ans[i], ans[j] + 1)

        return max(ans)