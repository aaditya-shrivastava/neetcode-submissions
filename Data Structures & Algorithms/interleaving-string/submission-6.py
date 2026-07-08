class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # n1, n2, n3 = len(s1), len(s2), len(s3)
        # if n1 + n2 != n3:
        #     return False
        # dp = [[False] * (n2 + 1) for _ in range(n1 + 1)]
        # dp[0][0] = True
        # for i in range(n1 + 1):
        #     for j in range(n2 + 1):
        #         if i > 0 and s1[i - 1] == s3[i + j - 1]:
        #             dp[i][j] = dp[i][j] or dp[i - 1][j]
        #         if j > 0 and s2[j - 1] == s3[i + j - 1]:
        #             dp[i][j] = dp[i][j] or dp[i][j - 1]
        # return dp[n1][n2]


        if len(s1) + len(s2) != len(s3):
            return False
        dp = [[False] * (len(s2)+1) for i in range(len(s1)+1)]
        dp[len(s1)][len(s2)] = True
        for i in range(len(s1),-1,-1):
            for j in range(len(s2),-1,-1):
                if i < len(s1) and s1[i] == s3[i+j] and dp[i+1][j]:
                    dp[i][j] = True 
                if j < len(s2) and s2[j] == s3[i+j] and dp[i][j+1]:
                    dp[i][j] = True
        return dp[0][0]
        # dp = {}
        # def dfs(i,j):
        #     if i == len(s1) and j == len(s2):
        #         return True
        #     if (i, j) in dp:
        #         return dp[(i,j)]
        #     if i < len(s1) and s1[i] == s3[i + j] and dfs(i + 1, j):
        #         return True
        #     if j < len(s2) and s2[j] == s3[i + j] and dfs(i, j + 1):
        #         return True
        #     dp[(i,j)] = False
        #     return False
        # return dfs(0,0)