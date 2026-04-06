class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2 == 1:
            return False
        
        target = sum(nums) // 2
        dp = set()
        dp.add(0)
        
        for i in range(len(nums) - 1, -1, -1):
            temp_dp = dp.copy()
            for t in dp:
                temp_dp.add(t + nums[i])
            dp = temp_dp

        return target in dp
            



        