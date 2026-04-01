class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        map = {i:[] for i in range(n)}

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i+1, n):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)

                map[i].append([dist, j])
                map[j].append([dist, i])

        
        visited = set()
        minHeap = [[0, 0]]
        totalCost = 0

        while len(visited) != n:
            cost, i = heapq.heappop(minHeap)

            if i in visited:
                continue
            
            visited.add(i);
            totalCost += cost

            for neiCost, nei in map[i]:
                if nei not in visited:
                    heapq.heappush(minHeap, [neiCost, nei])

        return totalCost
        