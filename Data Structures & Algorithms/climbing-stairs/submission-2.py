class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        n1, n2 = 1, 1

        for i in range(n - 1):
            n1 = n1 + n2
            n2 = n1 - n2

        return n1
        