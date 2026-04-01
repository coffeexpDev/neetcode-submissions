class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # create a hashmap to maintain edges and costs between nodes
        edges = defaultdict(list)
        # add connecting nodes to nodes map from input array
        for u, v, w in times:
            edges[u].append((v, w))

        visited = set()
        minheap = [(0, k)]
        time = 0

        while minheap:
            w1, n1 = heapq.heappop(minheap)
            # if node is already visited, skip
            if n1 in visited:
                continue
            # add node to visited set
            visited.add(n1)
            # set max time to react respective node
            time = max(time, w1)
            # iterate through respective edges from n1 node
            for n2, w2 in edges[n1]:
                # if destination node is not already visited, add to minheap
                if not n2 in visited:
                    heapq.heappush(minheap, ((w2 + w1), n2))

        # return time only if all nodes are visited, else -1
        return time if len(visited) == n else -1

        