import heapq
class Solution:
    def shortestPath(self,n, m, edges):
        adj = [[] for _ in range(n+1)]
        for u , v , wt in edges:
            adj[u].append((v,wt))
            adj[v].append((u,wt))
        dist = [10**9] * (n+1)
        par = [-1]*(n+1)
        dist[1] = 0
        par[1] = 1
        q = []
        heapq.heappush(q,(0,1))
        while q:
            d , node = heapq.heappop(q)
            if d > dist[node]:
                continue 
            for nei , wt in adj[node]:
                new_d = d + wt
                if new_d < dist[nei]:
                    dist[nei] = new_d
                    par[nei] = node
                    heapq.heappush(q,(new_d,nei))
        if dist[n] == 10**9:
            return[-1]
        path = []
        node = n
        while par[node] != node:
            path.append(node)
            node = par[node]
        path.append(1)
        path.reverse()
        return [dist[n]] + path