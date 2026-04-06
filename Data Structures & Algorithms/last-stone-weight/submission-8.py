class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        minheap = [-s for s in stones]
        heapq.heapify(minheap)

        while len(minheap) > 1:
            s1 = heapq.heappop(minheap)
            s2 = heapq.heappop(minheap)

            if s1 < s2:
                heapq.heappush(minheap, -1 * (s2 - s1))

        minheap.append(0)
        return abs(minheap[0])
        