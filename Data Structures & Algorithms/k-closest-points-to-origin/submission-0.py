class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for i in range(len(points)):
            x, y = points[i]
            distance = math.sqrt(x**2 + y**2)
            distances.append((distance, points[i]))
        distances.sort()
        result = []
        for i in range(k):
            result.append(distances[i][1])
        return result