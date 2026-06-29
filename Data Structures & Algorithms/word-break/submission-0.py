class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        ans = [False] * (len(s)+1)
        ans[0] = True
        for i in range(1,len(s)+1):
            for w in wordDict:
                if i >= len(w) and ans[i - len(w)] and s[i - len(w):i] == w:
                    ans[i] = True
                    break
        print(ans[-1])
        return ans[-1]