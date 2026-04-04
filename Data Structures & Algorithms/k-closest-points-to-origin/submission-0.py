class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap = []
        heapq.heapify(minheap)

        for i, p in enumerate(points):
            dist = p[0]**2 + p[1]**2
            heapq.heappush(minheap, (dist, p[0], p[1]))
        
        res = []
        while k > 0:
            d, x, y = heapq.heappop(minheap)

            res.append([x, y])
            k -= 1
        
        return res


        
        