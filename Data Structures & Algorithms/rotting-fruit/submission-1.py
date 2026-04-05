class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [[1,0],[-1,0], [0,1],[0,-1]]
        rows, cols = len(grid), len(grid[0])
        fresh = 0
        time = 0
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))
        
        while fresh and q:
            for i in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (row not in range(rows) or col not in range(cols) or 
                        grid[row][col] != 1):
                        continue
                    
                    grid[row][col] = 2
                    fresh -= 1
                    q.append((row, col))
            time += 1

        return time if fresh == 0 else -1
        