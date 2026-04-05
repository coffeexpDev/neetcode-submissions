class Solution:
    def rob(self, nums: List[int]) -> int:

        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        return max(self.houseRobber1(nums[1:]), self.houseRobber1(nums[:-1]))


    
    def houseRobber1(self, nums):
        rob, rob1 = 0, 0

        for n in nums:
            temp = max(rob1, n + rob)
            rob = rob1
            rob1 = temp
        return rob1

        