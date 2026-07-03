class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        ans = [False] * (len(s)+1)
        ans[len(s)] = True
        for i in range(len(s), -1, -1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i: i + len(w)] == w:
                    ans[i] = ans[i + len(w)]
                if ans[i]:
                    break
        return ans[0]