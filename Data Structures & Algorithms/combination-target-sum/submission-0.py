class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        results = []
        def backtrack(remain, current_combination, start_index):
            if remain == 0:
                results.append(list(current_combination))
                return
            elif remain < 0:
                return
            for i in range(start_index, len(nums)):
                num = nums[i]
                current_combination.append(num)
                backtrack(remain - num, current_combination, i)
                current_combination.pop()

        backtrack(target, [], 0)
        return results