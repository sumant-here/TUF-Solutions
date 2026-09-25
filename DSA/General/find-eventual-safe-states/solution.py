from collections import deque
class Solution:
    def eventualSafeNodes(self, V, adj):
        rev = [[] for _ in range(V)]
        outd = [0] * V 
        #ebe out degre calculate koriba aau grapg reverse koriba .
        for i in range(V):
            outd[i] = len(adj[i])
            for nei in adj[i]:
                rev[nei].append(i)
        q  = deque()
        #ebe terminal Node dekhiba 
        for i in range(V):
            if outd[i] == 0 :
                q.append(i)
        safe = []
        while q :
            node = q.popleft()
            safe.append(node)
            for nei in rev[node]:
                outd[nei] -=1
                if outd[nei] == 0 :
                    q.append(nei)
        safe.sort()
        return safe
            
       