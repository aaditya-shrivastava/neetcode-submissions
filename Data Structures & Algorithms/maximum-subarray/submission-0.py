class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxnum = nums[0]
        curMax = nums[0]

        for i in range (1, len(nums)):
            curMax = max(nums[i], curMax + nums[i])
            maxnum = max(maxnum, curMax)

        return maxnum
