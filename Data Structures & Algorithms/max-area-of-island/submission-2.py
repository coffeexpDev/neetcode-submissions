class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        rows, cols = len(grid), len(grid[0])
        res = 0
        visited = set()

        def dfs(r, c):
            if (r not in range(rows) or c not in range(cols) or
                (r, c) in visited or grid[r][c] == 0):
                return 0
            
            visited.add((r, c))

            res = 1
            for dr, dc in directions:
                row, col = r + dr, c + dc
                res += dfs(row, col)
            
            return res

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area = dfs(r, c)
                    res = max(res, area)

        return res
        