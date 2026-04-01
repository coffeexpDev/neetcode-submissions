class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")]*n
        prices[src] = 0
        
        adj = [[] for i in range(n)]

        for s, d, p in flights:
            adj[s].append([d, p])

        q = deque([(0, src, 0)]) # [price, node, stops]

        while(q):
            price, node, stops = q.popleft()

            if stops > k:
                continue

            for n, p in adj[node]:
                nextPrice = p + price
                if nextPrice < prices[n]:
                    prices[n] = nextPrice
                    q.append((nextPrice, n, stops + 1))

        return prices[dst] if prices[dst] != float("inf") else -1 
        