
class Solution:
    def dfsOfGraph(self, V, edges):
        adj = [[] for _ in range(V)]
        vis = [0] * (V)
        res = []
        for u , v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        def dfs(node):
            vis[node] = 1
            res.append(node)
            for child in adj[node]:
                if not vis[child]:
                    dfs(child)
        dfs(0)
        return res
    
    def bfsOfGraph(self, V, edges):
        adj = [[] for _ in range (V)]
        for u , v in edges:
            adj[u].append(v)
            adj[v].append(u)
        vis = [0] * (V)
        res = []
        q = deque()
        q.append(0)
        vis[0] = 1
        while q:
            node = q.popleft()
            res.append(node)
            for child in adj[node]:
                if not vis[child]:
                    vis[child] = 1
                    q.append(child)
        return res


      