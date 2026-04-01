class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        return max(self.findLoot(nums[1:]), self.findLoot(nums[:-1]))

    def findLoot(self,nums):
        # house robber 1 implentation
        rob1, rob2 = 0, 0
        for n in nums:
            t = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = t

        return rob2
        