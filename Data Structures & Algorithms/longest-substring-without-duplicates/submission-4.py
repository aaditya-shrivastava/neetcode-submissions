class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = set()
        max_count = 0
        left = 0
        for right in range(len(s)):
            while s[right] in ans:
                ans.remove(s[left])
                left += 1
            ans.add(s[right])
            max_count = max(max_count, right - left + 1)
        return max_count