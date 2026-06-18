class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            ans.append(1)
            for j in range(len(nums)):
                if i != j:
                    ans[i] = ans[i] * nums[j]
        return ans