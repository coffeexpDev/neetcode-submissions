class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        sorted_str = sorted(strs)
        first = sorted_str[0]
        last = sorted_str[n-1]
        min_len = len(first)
        res = ""
        for i in range(min_len):
            if first[i] != last[i]:
                return res
            res += first[i]
        
        return res
            
        