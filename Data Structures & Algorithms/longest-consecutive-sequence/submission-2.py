class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        map = defaultdict(int)
        res = 0

        for num in nums:
            print(f"{map}")
            if not map[num]:
                map[num] = map[num-1] + map[num+1] + 1
                map[num - map[num-1]] = map[num]
                map[num + map[num+1]] = map[num]
                res = max(res, map[num])

        return res