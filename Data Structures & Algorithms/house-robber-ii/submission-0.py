class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def helper(nums):
            prev = curr = 0
            for n in nums:
                prev, curr = curr, max(curr, prev + n)
            return curr
        return max(helper(nums[:-1]), helper(nums[1:]))