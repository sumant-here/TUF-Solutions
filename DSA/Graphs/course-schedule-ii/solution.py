from collections import deque
class Solution:
    def findOrder(self, N, arr):
        adj = [[] for _ in range(N)]
        ind = [0] * N
        for course , pre in arr:
            adj[pre].append(course)
            ind[course] += 1
        q  = deque()
        for i in range(N):
            if ind[i] == 0 :
                q.append(i)
        an =[]
        while q:
            node = q.popleft()
            an.append(node)
            for nei in adj[node]:
                ind[nei] -= 1
                if ind[nei] ==0:
                    q.append(nei)
        if len(an) == N:
            return an
        return []
        