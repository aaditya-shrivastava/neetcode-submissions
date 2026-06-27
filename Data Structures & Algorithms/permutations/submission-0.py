class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backtrack(index, current_permutation):
            if index == len(nums):
                result.append(list(current_permutation))
                return
            for i in range(len(nums)):
                if nums[i] not in current_permutation:
                    current_permutation.append(nums[i])
                    backtrack(index + 1, current_permutation)
                    current_permutation.pop()

        backtrack(0, [])
        return result