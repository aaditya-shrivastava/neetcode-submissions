class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        for l in range(len(nums)-k+1):
            t = l
            r = l + k-1
            maxE = float('-inf')
            while t <= r :
                maxE = max(maxE, nums[t])
                t += 1
            ans.append(maxE)
        return ans