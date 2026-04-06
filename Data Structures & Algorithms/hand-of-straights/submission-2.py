class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
            
        count = defaultdict(int)
        
        for n in hand:
            count[n] += 1
            
        minheap = list(count.keys())
        heapq.heapify(minheap)

        while minheap:
            val = minheap[0]

            for i in range(val, val + groupSize):
                if i not in count:
                    return False

                count[i] -= 1
                if count[i] == 0:
                    if i not in minheap:
                        return False
                    heapq.heappop(minheap)
        
        return True
        