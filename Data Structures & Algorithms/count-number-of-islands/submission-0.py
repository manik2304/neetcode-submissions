from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid: return 0

        n = 0 # number of islands
        rows = len(grid) # num of rows
        cols = len(grid[0]) # num of columns
        seen = set()

        def bfs(r,c):
            nonlocal rows, cols
            q = deque()
            q.append((r,c))
            neighbours = [(0,-1),(0,1), (-1,0), (1,0)]

            while q:
                r, c = q.popleft()
                for (i,j) in neighbours:
                    if (0<=r+i < rows and 0<= c+j < cols
                        and (r+i,c+j) not in seen
                        and grid[r+i][c+j] == '1'):
                        seen.add((r+i,c+j))
                        q.append((r+i,c+j))


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r,c) not in seen:
                    seen.add((r,c))
                    bfs(r,c)
                    n += 1

        return n
        