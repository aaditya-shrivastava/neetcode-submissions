class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        for ele in strs:
            word = ''.join(sorted(ele))
            if word not in ans:
                ans[word] = []
            ans[word].append(ele)
        return list(ans.values())