class Solution:
    def findMin(self, nums: List[int]) -> int:
        mini = float('inf')
        for num in nums:
             mini = min(mini, num)
        return mini