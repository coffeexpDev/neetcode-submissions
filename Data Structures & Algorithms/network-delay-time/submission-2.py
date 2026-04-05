class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)
        for u, v, w in times:
            edges[u].append([v, w])
        
        visited = set()
        minheap = [(0, k)]
        res = 0

        while minheap:
            w, u = heapq.heappop(minheap)
            if u in visited:
                continue
            
            visited.add(u)
            res = max(res, w)
            for v, w2 in edges[u]:
                if v not in visited:
                    heapq.heappush(minheap, (w + w2, v))
        
        return res if len(visited) == n else - 1

        