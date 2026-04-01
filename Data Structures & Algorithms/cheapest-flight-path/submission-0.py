class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        costs = [float("inf")] * n
        costs[src] = 0

        for i in range(k+1):
            temp = costs.copy()

            for s, d, c in flights:
                if costs[s] == float("inf"):
                    continue
                
                if costs[s] + c < temp[d]:
                    temp[d] = costs[s] + c

            costs = temp

        return costs[dst] if costs[dst] != float("inf") else -1