from collections import deque
class Solution:
    def isBipartite(self, V, edges):
        adj = [[] for _ in range(V)]
        for u , v in edges:
            adj[u].append(v)
            adj[v].append(u)

        set_a  = set()
        set_b = set()
        vis = set()
        for i in range(V):
            if i in vis:
                continue     
            q = deque()
            q.append(i)
            vis.add(i)
            set_a.add(i)
            while q:
                node = q.popleft()
                for nei in adj[node]:
                    if nei in set_a:
                        if node in set_a:
                            return False
                    if nei in set_b:
                        if node in set_b:
                            return False 
                    if nei not in vis:
                        q.append(nei)
                        vis.add(nei)
                        if node in set_a:
                            set_b.add(nei)
                        else:
                            set_a.add(nei)
        return True 


