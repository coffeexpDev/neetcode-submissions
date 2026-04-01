class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visited = set() 
        minHeap = [[grid[0][0],0,0]] #[t, r, c]

        while minHeap:
            t, r, c = heapq.heappop(minHeap)

            if r == n-1 and c == n-1:
                return t
            
            for dr, dc in directions:
                row, col = r + dr, c + dc

                if (row not in range(n) or col not in range(n) or (row, col) in visited):
                    continue
                
                visited.add((row, col))
                heapq.heappush(minHeap, [max(t, grid[row][col]), row, col])

        return res


        
        