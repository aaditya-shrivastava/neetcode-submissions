class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        m, n = len(heights), len(heights[0])
        pacific_reachable = [[False] * n for _ in range(m)]
        atlantic_reachable = [[False] * n for _ in range(m)]
        result = []
        def dfs(r, c, reachable_matrix):
            reachable_matrix[r][c] = True
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and not reachable_matrix[nr][nc] and heights[nr][nc] >= heights[r][c]:
                    dfs(nr, nc, reachable_matrix)
        for r in range(m):
            dfs(r, 0, pacific_reachable)
        for c in range(n):
            dfs(0, c, pacific_reachable)
        for r in range(m):
            dfs(r, n - 1, atlantic_reachable)
        for c in range(n):
            dfs(m - 1, c, atlantic_reachable)
        for r in range(m):
            for c in range(n):
                if pacific_reachable[r][c] and atlantic_reachable[r][c]:
                    result.append([r, c])
        return result