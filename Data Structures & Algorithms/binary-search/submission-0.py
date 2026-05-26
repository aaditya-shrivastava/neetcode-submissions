class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for el in range(len(nums)):
            if nums[el] == target:
                return el
        else: return -1