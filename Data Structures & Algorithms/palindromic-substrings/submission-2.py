class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0

        def countPalindromes(l, r):
            nonlocal count
            while l in range(len(s)) and r in range(len(s)) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1

        for i in range(len(s)):
            # for odd string length
            l, r = i, i
            countPalindromes(l, r)
            # for even string length
            l, r = i, i + 1
            countPalindromes(l, r)

        return count
        