class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # SOLUTION 1
        # total_gas = 0
        # curr_gas = 0
        # res = 0 # starting station index to be returned

        # for i in range(len(gas)):
        #     total_gas += gas[i] - cost[i]
        #     curr_gas += gas[i] - cost[i]

        #     if curr_gas < 0:
        #         curr_gas = 0
        #         res = i + 1

        # return res if not total_gas < 0 else -1

        # SOLUTION 2
        # # initial check to see if cycle is possible
        if sum(gas)< sum(cost):
            return -1
        tank = 0
        startIdx = 0

        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            
            if tank < 0:
                tank = 0
                startIdx = i + 1
        
        return startIdx
        