class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]

        # purpose of rank?: to maintain the size of connections for each node
        # initial value is 1 for all nodes
        # used for optimization
        rank = [1] * n

        def find(n1):
            res = n1

            while res != par[res]:
                par[res] = par[par[res]] # setting grand-parent if available
                res = par[res]

            return res

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return 0
            
            if rank[p2] > rank[p1]:
                par[p1] = p2
                rank[p2] += rank[p1]
            else:
                par[p2] = p1
                rank[p1] += rank[p2]

            return 1
        
        res = n

        for n1, n2 in edges:
            res -= union(n1, n2)
        
        return res

        