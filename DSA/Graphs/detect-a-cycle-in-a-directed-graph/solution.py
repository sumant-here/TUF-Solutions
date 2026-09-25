from collections import deque
class Solution:
    def isCyclic(self, N, adj):
        inde = [0] * N
        for i in range(N):
            for nei in adj[i]:
                inde[nei] +=1
        q = deque()
        for i in range(N):
            if inde[i] == 0 :
                q.append(i)
        count = 0 
        while q:
            node = q.popleft()
            count += 1
            for nei in adj[node]:
                inde[nei] -= 1
                if inde[nei] == 0 :
                    q.append(nei)
        if count == N:
            return False
        return True
        