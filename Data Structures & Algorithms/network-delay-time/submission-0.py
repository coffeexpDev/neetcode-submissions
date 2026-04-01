class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)

        for u, v, w in times:
            edges[u].append((v, w))

        visited = set()
        minheap = [(0, k)]
        time = 0

        while minheap:
            w1, n1 = heapq.heappop(minheap)

            if n1 in visited:
                continue

            visited.add(n1)
            time = max(time, w1)
            for n2, w2 in edges[n1]:
                if not n2 in visited:
                    heapq.heappush(minheap, ((w2 + w1), n2))

        return time if len(visited) == n else -1

        