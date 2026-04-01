class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n
        prices[src] = 0

        for i in range(k+1):
            temp = prices.copy()

            for start, end, price in flights:
                if prices[start] == float("inf"):
                    continue
                if price + prices[start] < temp[end]:
                    temp[end] = price + prices[start]
            prices = temp
        
        return prices[dst] if prices[dst] != float("inf") else -1