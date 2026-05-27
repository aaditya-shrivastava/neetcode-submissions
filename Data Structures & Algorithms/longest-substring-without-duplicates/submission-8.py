class Solution:
        def lengthOfLongestSubstring(self, s: str) -> int:
            ans = ""
            max_len = 0
            for ch in s:
                if ch in ans:
                    ans = ans[ans.index(ch)+1:]
                ans += ch
                max_len = max(max_len, len(ans))
            return max_len