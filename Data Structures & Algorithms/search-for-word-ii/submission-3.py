class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False
    
    def addWord(self, word:str):
        cur = self

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        
        cur.word = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        root = TrieNode()

        for w in words:
            root.addWord(w)

        rows, cols = len(board), len(board[0])
        res, visited = set(), set()

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(r, c, node, word):
            if (r not in range(rows) or c not in range(cols) or 
                (r, c) in visited or board[r][c] not in node.children):
                return
            
            visited.add((r, c))

            node = node.children[board[r][c]]
            word += board[r][c]

            if node.word == True:
                res.add(word)

            for dr, dc in directions: 
                dfs(r + dr, c + dc, node, word)

            visited.remove((r, c))
        
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root, "")
        
        return list(res)
            

                

        

        
        
        