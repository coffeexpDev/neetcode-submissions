class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        sortedArray = sorted(strs)
        minLen = len(sortedArray[0])
        res = ""
        for i in range(minLen):
            if sortedArray[0][i] != sortedArray[n-1][i]:
                return res
            res += sortedArray[0][i]
        
        return res
            
        