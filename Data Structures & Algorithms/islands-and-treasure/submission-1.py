class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        rows, cols = len(grid), len(grid[0])
        INF = 2147483647

        def dfs(r, c, dist):
            # exit conditions
            if (r not in range(rows) or c not in range(cols) or
                grid[r][c] == -1 or dist > grid[r][c]):
                return

            grid[r][c] = dist
            for dr, dc in directions:
                row, col = r + dr, c + dc
                dfs(row, col, dist + 1)



        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==0:
                    dfs(r, c, 0)
        