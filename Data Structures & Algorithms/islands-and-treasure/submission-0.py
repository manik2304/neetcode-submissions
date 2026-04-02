from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        sources = []
        seen = set()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    sources.append((r,c,0))
                    seen.add((r,c))


        q = deque(sources)

        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        while q:
            r,c,d = q.popleft()
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if (0<=nr<rows and 0<=nc<cols
                    and (nr,nc) not in seen
                    and grid[nr][nc] > 0):
                    q.append((nr,nc,d+1))
                    seen.add((nr,nc))
                    grid[nr][nc] = d+1

            




        