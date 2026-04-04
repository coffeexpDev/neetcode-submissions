class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        rows, cols = len(board), len(board[0])

        def dfs(r, c, i):
            if i == len(word):
                return True
                
            if (r not in range(rows) or c not in range(cols) or board[r][c] == '#' or word[i] != board[r][c]):
                return False

            board[r][c] = '#'
            res = False
            for dr, dc in directions:
                row, col = r + dr, c + dc
                res = res or dfs(row, col, i + 1)
            
            board[r][c] = word[i]
            return res

        
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True

        return False