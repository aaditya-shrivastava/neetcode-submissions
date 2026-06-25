class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        fresh_fruits = 0
        q = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh_fruits += 1
                elif grid[r][c] == 2:
                    q.append((r, c))
        minutes = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while q and fresh_fruits > 0:
            minutes += 1
            level_size = len(q)
            for _ in range(level_size):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh_fruits -= 1
                        q.append((nr, nc))
        if fresh_fruits == 0:
            return minutes
        else:
            return -1