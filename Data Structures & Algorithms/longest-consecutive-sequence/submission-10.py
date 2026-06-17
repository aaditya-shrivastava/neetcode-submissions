class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # if len(nums) == 0: return 0
        # new_nums = sorted(set(nums))
        # count = 1
        # max_count = 1
        # for i in range(1, len(new_nums)):
        #     if new_nums[i - 1] + 1 == new_nums[i]:
        #         count += 1
        #     else:
        #         count = 1
        #     max_count = max(max_count, count)
        # return max_count
        if not nums:
            return 0
        num_set = set(nums)
        max_length = 0    
        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_length = 1
                while current_num + 1 in num_set:
                    current_num += 1
                    current_length += 1
                max_length = max(max_length, current_length)
        return max_length