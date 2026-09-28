import heapq
class Solution:
    def countPaths(self, n, roads):
        adj = [[] for _ in range(n)]
        for u , v , t in roads:
            adj[u].append((v,t))
            adj[v].append((u,t))
        inf = float('inf')
        time = [inf] * n 
        ways =[0] *n
        time[0] = 0 
        ways[0] = 1
        q = []
        heapq.heappush(q,(0,0))
        mod = 10**9 + 7 
        while q:
            ti , node = heapq.heappop(q)
            if ti > time[node]:
                continue 
            for nei ,tim in adj[node]:
                new_t = ti + tim
                if new_t < time[nei]:
                    time[nei] = new_t
                    ways[nei] =ways[node]
                    heapq.heappush(q,(new_t,nei))
                elif new_t == time[nei]:
                    ways[nei] = (ways[nei]+ways[node]) % mod
        return ways[n-1]
            
        
        
                
      