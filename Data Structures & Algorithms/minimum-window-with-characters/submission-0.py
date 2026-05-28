class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s) : return ""
        need = {}
        for c in t:
            need[c] = need.get(c, 0) + 1
        l = 0
        count = len(t)
        min_len = float('inf')
        start = 0
        for r in range(len(s)):
            if s[r] in need:
                if need[s[r]] > 0:
                    count -= 1
                need[s[r]] -= 1
            while count == 0:
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    start = l
                if s[l] in need:
                    need[s[l]] += 1
                    if need[s[l]] > 0:
                        count += 1
                l += 1
        return "" if min_len == float('inf') else s[start:start + min_len]