class Solution:
    def solve(self, board: List[List[str]]) -> None:

        # step 1: capture unsurrounded Os ( O -> # )
        # step 2: capture surrounded Os ( O -> X )
        # step 1: uncapture unsurrounded Os ( # -> O )
        rows, cols = len(board), len(board[0])

        def capture(r, c):
            if (r not in range(rows) or c not in range(cols) or
                board[r][c]!='O'):
                return
            
            board[r][c] = '#'
            capture(r + 1, c)
            capture(r - 1, c)
            capture(r, c + 1)
            capture(r, c - 1)
        
        # step 1
        for r in range(rows):
            for c in range(cols):
                if r in [0, rows - 1] or c in [0, cols - 1]:
                    capture(r, c)

        # step 2
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'

        # step 3
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == '#':
                    board[r][c] = 'O'
        