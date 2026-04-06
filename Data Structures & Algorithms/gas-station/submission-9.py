class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        tgas, cgas = 0, 0
        start = 0

        for i in range(len(gas)):
            tgas += gas[i] - cost[i]
            cgas += gas[i] - cost[i]

            if cgas < 0:
                cgas = 0
                start = i + 1
        
        return start if tgas >= 0 else -1
        