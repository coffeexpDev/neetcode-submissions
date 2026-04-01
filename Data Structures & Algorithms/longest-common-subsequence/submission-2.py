class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) < len(text2):
            text1, text2 = text2, text1

        dp = [0] * (len(text2)+1)

        for i in range(len(text1) - 1, -1, -1):
            prev = 0          # represents dp[i+1][j+1] — diagonal value
            for j in range(len(text2) - 1, -1, -1):
                temp = dp[j]          # save dp[j] BEFORE overwriting it
                          # (next iteration needs it as the diagonal)
                if text1[i] == text2[j]:
                    dp[j] = 1 + prev  # prev = old dp[j+1] = diagonal
                else:
                    dp[j] = max(dp[j], dp[j+1])
                          # dp[j]   = old value below (not yet touched)
                          # dp[j+1] = already updated this row (right)
                prev = temp           # pass the saved dp[j] forward as next j's diagonal

        return dp[0]
        