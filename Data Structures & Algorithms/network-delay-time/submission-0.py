class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = [[] for _ in range(n + 1)]
        for u, v, t in times:
            adj[u].append((v, t))
        distances = [float('inf')] * (n + 1)
        distances[k] = 0
        min_heap = [(0, k)]
        while min_heap:
            time, u = heapq.heappop(min_heap)
            if time > distances[u]:
                continue
            for v, t_uv in adj[u]:
                if distances[u] + t_uv < distances[v]:
                    distances[v] = distances[u] + t_uv
                    heapq.heappush(min_heap, (distances[v], v))
        max_time = 0
        for i in range(1, n + 1):
            if distances[i] == float('inf'):
                return -1
            max_time = max(max_time, distances[i])
        return max_time