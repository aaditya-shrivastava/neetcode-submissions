class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num = nums1 + nums2
        nums = sorted(num)
        l, r = len(nums1), len(nums2)
        mid = len(nums) // 2
        ans = 0
        if len(nums) % 2 != 0:
            ans = nums[mid]
        else:
            ans = (nums[mid - 1] + nums[mid]) / 2
        return ans