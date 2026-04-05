class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0

        def findLongestPalindrome(l, r):
            nonlocal res, resLen
            while l in range(len(s)) and r in range(len(s)) and s[l] == s[r]:
                if r - l + 1 > resLen:
                    res = s[l: r + 1]
                    resLen = r - l + 1
                l -= 1
                r += 1

        for i in range(len(s)):
            # for odd string length
            l, r = i, i
            findLongestPalindrome(l, r)

            # for even string length
            l, r = i, i + 1
            findLongestPalindrome(l, r)
    
        return res

        