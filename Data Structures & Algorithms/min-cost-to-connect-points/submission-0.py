class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        edges = {i:[] for i in range(n)}

        # build the adjacency list for each point [cost, point]
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                edges[i].append([dist, j])
                edges[j].append([dist, i])

        res = 0 # overall cost
        visited = set() # to make sure we don't visit the same node each time
        minheap = [[0, 0]]
        # exit condition, just enough to connect all points
        while len(visited) != n:
            cost, i = heapq.heappop(minheap)
            # check is point is already visited, if visited -> continue to the next loop
            if i in visited:
                continue
            
            visited.add(i)
            res += cost

            for neiCost, nei in edges[i]:
                if nei not in visited:
                    heapq.heappush(minheap, [neiCost, nei])

        
        return res



        