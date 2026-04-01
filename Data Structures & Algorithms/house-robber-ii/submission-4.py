class Solution:
    def rob(self, nums: List[int]) -> int:

        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]
        
        return max(self.find_loot(nums[:-1]), self.find_loot(nums[1:]))

    def find_loot(self, nums):
            rob1, rob2 = 0, 0
            for n in nums:
                t = max(rob2, n + rob1)
                rob1 = rob2
                rob2 = t

            return rob2
        