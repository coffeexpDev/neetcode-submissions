class Solution:
    def rob(self, nums: List[int]) -> int:

        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        def find_loot(start, end):
            rob1, rob2 = 0, 0
            for n in nums[start:end]:
                t = max(rob2, n + rob1)
                rob1 = rob2
                rob2 = t

            return rob2
        
        return max(find_loot(0, len(nums)-1), find_loot(1, len(nums)))
        