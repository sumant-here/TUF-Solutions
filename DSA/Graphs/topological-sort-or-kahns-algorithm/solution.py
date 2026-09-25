from collections import deque
class Solution:
    def topoSort(self, V, adj):
        inde = [0] * V
        for i in range(V):
            for nei in adj[i]:
                inde[nei] += 1
        q = deque()
        for i in range(V):
            if inde[i] == 0:
                q.append(i)
        ans = []
        while q:
            node = q.popleft()
            ans.append(node)
            for nei in adj[node]:
                inde[nei] -= 1
                if inde[nei]  == 0:
                    
                    q.append(nei)
        return ans 
        
                
       
