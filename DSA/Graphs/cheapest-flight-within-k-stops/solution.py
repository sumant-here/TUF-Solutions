from collections import deque
from typing import List

class Solution:
    def CheapestFlight(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        adj = [[] for _ in range(n)]
        for u, v, pri in flights:
            adj[u].append((v, pri))
        inf = 10**9

        dist = [inf] * n
        dist[src] = 0

        q = deque()
        q.append((0, src, 0))          # (cost, node, edges used)

        while q:
            cost, node, stop = q.popleft()

            if stop > K:               # already used K+1 edges, can't go further
                continue

            for nei, pri in adj[node]:
                new_c = cost + pri
                if new_c < dist[nei]:
                    dist[nei] = new_c
                    q.append((new_c, nei, stop + 1))

        return -1 if dist[dst] == inf else dist[dst]
        