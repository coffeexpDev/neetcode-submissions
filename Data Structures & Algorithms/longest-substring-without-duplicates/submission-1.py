class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map, l, res = {}, 0, 0

        for r in range(len(s)):
            if s[r] in map:
                l = max(map[s[r]]+1, l)
            map[s[r]] = r
            res = max(res, r - l + 1)

        return res

        
        