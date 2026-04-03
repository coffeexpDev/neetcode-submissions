class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gas = 0
        curr_gas = 0
        res = 0 # starting station index to be returned

        for i in range(len(gas)):
            total_gas += gas[i] - cost[i]
            curr_gas += gas[i] - cost[i]

            if curr_gas < 0:
                curr_gas = 0
                res = i + 1

        return res if not total_gas < 0 else -1
        