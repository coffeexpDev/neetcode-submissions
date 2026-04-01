class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def dfs(r, c, i):
            if i == len(word):
                return True
            # check boundary conditions
            if (r < 0 or c < 0 or r >= rows or c >= cols or
                word[i] != board[r][c] or board[r][c] == '#'):
                return False

            # mark r,c as visited using '#'
            board[r][c] = '#'
            # check all 4 directions from matching letter of word
            res = (
                dfs(r + 1, c, i + 1) or
                dfs(r - 1, c, i + 1) or
                dfs(r, c + 1, i + 1) or
                dfs(r, c - 1, i + 1)
            )

            # unmark r,c
            board[r][c] = word[i]
            return res
        
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        
        return False
        