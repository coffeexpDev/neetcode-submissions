class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        sortedArr = sorted(strs)
        first = sortedArr[0]
        last = sortedArr[n - 1]
        res = ""

        for i in range(len(first)):
            if first[i] != last[i]:
                return res
            res += first[i]

        return res
            
        