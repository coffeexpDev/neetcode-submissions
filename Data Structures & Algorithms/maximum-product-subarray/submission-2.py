class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        res = float("-inf")
        currMin, currMax = 1, 1

        for n in nums:
            if n == 0:
                currMin, currMax = 1, 1 

            tmp = n * currMax
            currMax = max(tmp, n * currMin, n)
            currMin = min(tmp, n * currMin, n)
            res = max(res, currMax)
        
        return res

        