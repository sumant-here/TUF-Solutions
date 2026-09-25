from collections import deque
class Solution:
    def numProvinces(self, adj):
        n = len(adj)
        vis = [0] * n 
        count = 0 
        for i in range(n):
            if vis[i] == 1:
                continue
            vis[i] = 1
            count += 1
            q = deque()
            q.append(i)
            while q :
                node = q.popleft()
                for nei in range(n):
                    if adj[node][nei] == 1 and vis[nei] == 0:
                        vis[nei]=1
                        q.append(nei)
        return count