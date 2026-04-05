class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n
        prices[src] = 0

        for i in range(k + 1):
            copy = prices.copy()
            for s, d, cost in flights:
                if prices[s] == float("inf"):
                    continue
                copy[d] = min(copy[d], cost + prices[s])

            prices = copy
        
        return prices[dst] if prices[dst] != float("inf") else -1
                
                
        
        