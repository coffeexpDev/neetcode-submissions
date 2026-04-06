class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dmap = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in dmap:
                return [dmap[diff], i]
            dmap[n] = i