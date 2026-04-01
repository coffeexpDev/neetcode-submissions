class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = 0
        resLen = 0
        def findPalindrome(i):
            nonlocal res, resLen
            # for odd length
            l, r = i, i
            while l>=0 and r <len(s) and s[l] == s[r]:
                if((r - l + 1) > resLen):
                    res = s[l: r + 1]
                    resLen = r - l + 1
                l -= 1
                r += 1
            

            # for even length
            l, r = i, i + 1
            while l>=0 and r <len(s) and s[l] == s[r]:
                if((r - l + 1) > resLen):
                    res = s[l: r + 1]
                    resLen = r - l + 1
                l -= 1
                r += 1
            
        for i in range(len(s)):
            findPalindrome(i)
        
        return res
            

        