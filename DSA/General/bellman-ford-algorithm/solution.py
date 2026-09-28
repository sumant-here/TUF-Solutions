class Solution:
    def bellman_ford(self, V, edges, S):
        INF = 10**9
        dist = [INF] * V
        dist[S] = 0

        for _ in range(V - 1):
            for u, v, wt in edges:
                if dist[u] != INF and dist[u] + wt < dist[v]:
                    dist[v] = dist[u] + wt

        # V-th pass: any further improvement means a negative cycle
        for u, v, wt in edges:
            if dist[u] != INF and dist[u] + wt < dist[v]:
                return [-1]

        return dist