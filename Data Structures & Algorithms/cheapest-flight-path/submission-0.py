class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        cost = [float('inf')] * n
        cost[src] = 0
        for _ in range(k + 1):
            temp = cost[:]
            for u, v, w in flights:
                if cost[u] != float('inf'):
                    temp[v] = min(temp[v], cost[u] + w)
            cost = temp
        return -1 if cost[dst] == float('inf') else cost[dst]