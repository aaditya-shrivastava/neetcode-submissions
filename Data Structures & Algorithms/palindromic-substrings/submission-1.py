class Solution:
    res = 0
    def countSubstrings(self, s: str) -> int:
        for i in range(len(s)):
            # Odd length
            self.helper(s, i, i)

            # Even length
            self.helper(s, i, i + 1)

        return self.res

    def helper(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            self.res += 1
            l -= 1
            r += 1