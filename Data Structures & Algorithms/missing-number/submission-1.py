class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num = len(nums)
        for i, n in enumerate(nums):
            num += i - n

        return num
        

        