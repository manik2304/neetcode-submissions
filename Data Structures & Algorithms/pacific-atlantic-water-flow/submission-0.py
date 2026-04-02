from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])

        pacific_seen = set()
        atlan_seen = set()

        for r in range(rows):
            pacific_seen.add((r,0))
            atlan_seen.add((r, cols-1))

        for c in range(cols):
            pacific_seen.add((0,c))
            atlan_seen.add((rows-1,c))

        def bfs(s):
            nonlocal rows, cols
            directions = [(1,0),(-1,0),(0,1),(0,-1)]
            q = deque(list(s))
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if (0<=nr<rows and 0<=nc<cols
                        and heights[nr][nc]>=heights[r][c]
                        and (nr,nc) not in s):
                        s.add((nr,nc))
                        q.append((nr,nc))

            return s

        pacific_seen = bfs(pacific_seen)
        atlan_seen = bfs(atlan_seen)

        results = []
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pacific_seen and (r,c) in atlan_seen:
                    results.append([r,c])

        return results




        