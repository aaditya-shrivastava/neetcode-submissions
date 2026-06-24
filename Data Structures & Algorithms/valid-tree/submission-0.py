class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
        if len(edges) != n - 1:
            return False
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visited = [False] * n
        visited_count = 0
        def dfs(u, parent):
            nonlocal visited_count
            visited[u] = True
            visited_count += 1
            for v in adj[u]:
                if v == parent:
                    continue
                if visited[v]:
                    return False
                if not dfs(v, u):
                    return False
            return True
        if not dfs(0, -1):
            return False
        return visited_count == n