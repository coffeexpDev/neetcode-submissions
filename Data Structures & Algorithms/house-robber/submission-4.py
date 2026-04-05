class Solution:
    def rob(self, nums: List[int]) -> int:
        rob, rob1 = 0, 0

        for n in nums:
            temp = max(rob1, n + rob)
            rob = rob1
            rob1 = temp
        
        return rob1
        