class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()
        while n not in visit:
            visit.add(n)
            n = self.sumOfSquares(n)

            if n == 1:
                return True
        return False


    def sumOfSquares(self, n: int) -> int:
        res = 0
        while n:
            r = n % 10
            res += r*r
            n = n // 10
        return res
        