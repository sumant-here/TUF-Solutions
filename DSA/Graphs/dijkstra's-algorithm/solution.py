import heapq
class Solution:
    def dijkstra(self, V, edges, S):
        adj =[[] for _ in range(V)]
        for u , v , wt in edges:
            adj[u].append((v,wt))
            adj[v].append((u,wt))
        dist = [10**9] * V
        dist[S] = 0 
        q = []
        heapq.heappush(q,(0,S))
        while q:
            d  , node = heapq.heappop(q)
            if d != dist[node]:
                continue
            for nei , wt in adj[node]:
                new_d = d + wt
                if new_d < dist[nei]:
                    dist[nei] = new_d
                    heapq.heappush(q,(new_d,nei))
        return dist