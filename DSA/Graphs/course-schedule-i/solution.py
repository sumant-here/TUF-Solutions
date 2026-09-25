from collections import deque
class Solution:
    def canFinish(self, N, arr):
        adj = [[] for _ in range(N)]
        ind =[0] * N
        #jou course neichi mu na sithe  . pre course koriki adj list re append koro and ind c +1
        for course , pre in arr:
            adj[pre].append(course)
            ind[course] += 1
        q = deque()
        for i in range(N):
            if ind[i] == 0:
                q.append(i)
        count = 0 
        while q :
            node = q.popleft()
            count += 1
            for nei in adj[node]:
                ind[nei] -= 1
                if ind[nei] == 0 :
                    q.append(nei)
        return count == N
            
            
            
        