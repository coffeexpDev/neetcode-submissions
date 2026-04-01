class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = {src:[] for src, dest in tickets}
        
        tickets.sort() #to sort the list lexicographically

        # add src -> dest to adjacency list map
        for src, dest in tickets:
            adj[src].append(dest)

        # starting airport is always "JFK" -> refer question
        res = ["JFK"]

        def dfs(src):
            # check completion condition
            if len(res) == len(tickets) + 1:
                return True
            # check if any flights are going out of src airport using adjacency list
            if src not in adj:
                return False
            

            temp = list(adj[src])
            for i, v in enumerate(temp):
                adj[src].pop(i)
                res.append(v)

                if dfs(v): return True

                adj[src].insert(i, v)
                res.pop()

            return False

        dfs("JFK")

        return res
        