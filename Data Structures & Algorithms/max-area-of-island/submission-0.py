from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid: return 0

        max_area = 0
        rows, cols = len(grid), len(grid[0])
        seen = set()

        def bfs(r,c):
            q = deque([(r,c)])
            area = 0
            directions = [(-1,0),(1,0),(0,-1),(0,1)]

            while q:
                r,c = q.popleft()
                area += 1
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if (0<=nr<rows and 0<=nc<cols
                        and (nr,nc) not in seen
                        and grid[nr][nc]==1):
                        seen.add((nr,nc))
                        q.append((nr,nc))
            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in seen:
                    seen.add((r,c))
                    area = bfs(r,c)
                    max_area = max(max_area, area)

        return max_area


        