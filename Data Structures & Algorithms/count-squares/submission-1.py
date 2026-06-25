class CountSquares:

    def __init__(self):
        self.points = defaultdict(int)
    def add(self, point):
        x, y = point
        self.points[(x, y)] += 1
    def count(self, point):
        x, y = point
        ans = 0

        for (nx, ny), cnt in self.points.items():

            if ny != y or nx == x:
                continue

            d = nx - x

            ans += (
                cnt *
                self.points.get((x, y + d), 0) *
                self.points.get((nx, y + d), 0)
            )

            ans += (
                cnt *
                self.points.get((x, y - d), 0) *
                self.points.get((nx, y - d), 0)
            )

        return ans