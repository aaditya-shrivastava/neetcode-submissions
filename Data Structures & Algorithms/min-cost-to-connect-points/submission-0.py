import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        vis = set()
        heap = [(0, 0)]
        ans = 0
        while len(vis) < n:
            cost, i = heapq.heappop(heap)
            if i in vis:
                continue
            vis.add(i)
            ans += cost
            for j in range(n):
                if j not in vis:
                    x1, y1 = points[i]
                    x2, y2 = points[j]
                    d = abs(x1 - x2) + abs(y1 - y2)
                    heapq.heappush(heap, (d, j))
        return ans