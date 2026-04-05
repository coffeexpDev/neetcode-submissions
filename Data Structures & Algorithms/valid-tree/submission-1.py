class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
        edgeMap = {i:[] for i in range(n)}
        for n1, n2 in edges:
            edgeMap[n1].append(n2)
            edgeMap[n2].append(n1)
        
        visited = set()
        def dfs(n, prev):
            if n in visited:
                return False
            
            visited.add(n)

            for node in edgeMap[n]:
                if node == prev:
                    continue
                if not dfs(node, n):
                    return False
            return True

        return dfs(0, -1) and len(visited) == n 
        