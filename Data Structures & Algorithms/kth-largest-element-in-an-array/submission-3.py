class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # nums.sort()
        # return nums[len(nums)-k]
        ans = 0

        for i in range(k):
            heapq.heapify_max(nums)
            ans = heapq.heappop(nums)
        return ans