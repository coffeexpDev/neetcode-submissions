class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        i = 0
        for j in range(len(prices)):
            if prices[j] < prices[i]:
                i = j
            else:
                maxProfit = max(maxProfit, prices[j] - prices[i])
        
        return maxProfit
        