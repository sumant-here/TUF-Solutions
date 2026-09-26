from collections import deque
class Solution:
    def shortestPath(self, N, M, edges):
        adj =[[] for _ in range(N)]
        ind = [0]* N
        #make graph
        for u , v, wt in edges:
            adj[u].append((v,wt))
            ind[v] += 1
        q = deque()
        for i in range(N):
            if ind[i] == 0 :
                q.append(i)
        topo = []
        while q:
            node = q.popleft()
            topo.append(node)
            for nei , wt in adj[node]:
                ind[nei] -= 1
                if ind[nei] == 0:
                    q.append(nei)
        dist =[float('inf')] * N
        dist[0] = 0 
        for node in topo:
            for nei, wt in adj[node]:
                dist[nei] =  min(dist[node]+ wt,dist[nei])
        #         if dist[node] + wt <dist[nei]:
        #             dist[nei] = dist[node]  + wt
        for i in range(N):
            if dist[i] == float('inf'):
                dist[i] = -1
        return dist
       