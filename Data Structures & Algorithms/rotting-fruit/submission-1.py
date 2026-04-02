from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        rows, cols = len(grid), len(grid[0])
        start = []
        fresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    start.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1

        if fresh == 0: return 0

        q = deque(start)
        days = 0
        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        while q:
            l = len(q)
            got_rotten = False

            for _ in range(l):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if (0<=nr<rows and 0<=nc<cols
                        and grid[nr][nc] == 1):
                        grid[nr][nc] = 2
                        q.append((nr,nc))
                        got_rotten = True
            
            if got_rotten: days += 1

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1: return -1

        return days



        