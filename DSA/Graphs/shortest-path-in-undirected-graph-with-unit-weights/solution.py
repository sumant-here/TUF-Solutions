class Solution:
    def shortestPath(self, edges, N, M):
        adj = [[]for _ in range(N)]
        for u , v in edges:
            adj[u].append(v)
            adj[v].append(u)
        dist =[-1] * N
        dist[0] = 0
        q = deque()
        q.append(0)
        while q:
            node = q.popleft()
            for nei in adj[node]:
                if dist[nei] == -1:
                    dist[nei] = dist[node] + 1
                    q.append(nei)
        return dist      