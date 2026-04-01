class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n # [1, 1, 1, 1, 1...n] n = num of columns

        for i in range(m-1): # m = num of rows
            newRow = [1] * n # [1, 1, 1, 1, 1...n] n = num of columns
            for j in range(n-2, -1, -1):
                newRow[j] = newRow[j + 1] + row[j]
            row = newRow
        
        return row[0]

        