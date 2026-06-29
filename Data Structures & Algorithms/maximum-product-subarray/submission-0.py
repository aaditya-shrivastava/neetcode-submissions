class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        dpMax = [0] * n
        dpMin = [0] * n
        dpMax[0] = dpMin[0] = ans = nums[0]
        for i in range(1, n):
            if nums[i] >= 0:
                dpMax[i] = max(nums[i], dpMax[i-1] * nums[i])
                dpMin[i] = min(nums[i], dpMin[i-1] * nums[i])
            else:
                dpMax[i] = max(nums[i], dpMin[i-1] * nums[i])
                dpMin[i] = min(nums[i], dpMax[i-1] * nums[i])
            ans = max(ans, dpMax[i])
        return ans