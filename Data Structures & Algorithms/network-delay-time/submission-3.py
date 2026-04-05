class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        edges = defaultdict(list)

        for u, v, w in times:
            edges[u].append([v, w])
        
        time = 0
        visited = set()
        minheap = [(0, k)]

        while minheap:
            w, u = heapq.heappop(minheap)

            if u in visited:
                continue
            
            visited.add(u)
            time = max(time, w)

            for v, w2 in edges[u]:
                if v not in visited:
                    heapq.heappush(minheap,(w + w2, v))
        
        return time if len(visited) == n else -1
        