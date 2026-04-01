class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # to keep track of Q positions and paths
        col = set()
        pdiag = set() # (r + c)
        ndiag = set() # (r - c)

        res = [] # to store output board
        board = [["."] * n for i in range(n)] # board for computing

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            for c in range(n):
                if c in col or (r + c) in pdiag or (r - c) in ndiag:
                    continue
                
                col.add(c)
                pdiag.add(r + c)
                ndiag.add(r - c)
                board[r][c] = "Q"

                backtrack(r + 1)

                col.remove(c)
                pdiag.remove(r + c)
                ndiag.remove(r - c)
                board[r][c] = "."

        backtrack(0)
        return res

        