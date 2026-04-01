class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:

        n = len(grid)
        visited = set()
        directions = [[1, 0],[-1, 0], [0, 1], [0, -1]]
        minheap = [[grid[0][0], 0, 0]] # [t, r, c]
        visited.add((0, 0)) # (row, col)
        
        while minheap:
            t, r, c = heapq.heappop(minheap)

            # boundary conditions to return result
            if r == (n - 1) and c == (n - 1):
                return t

            for dr, dc in directions:
                row, col = r + dr, c + dc
                # boundary conditions to invalidate (row, col)
                if (row not in range(n) or col not in range(n) or
                    (row, col) in visited):
                    continue
                
                visited.add((row, col))
                heapq.heappush(minheap, [max(t, grid[row][col]), row, col])