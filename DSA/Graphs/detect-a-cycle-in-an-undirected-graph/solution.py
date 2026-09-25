from collections import deque
class Solution:
    def isCycle(self, V: int, adj: list[list[int]]) -> bool:
        vis = set()
        for i in range (V):
            if i in vis:
                continue
            q = deque()
            q.append((i,-1))
            vis.add(i)
            while q:
                node,parent = q.popleft()
                for nei in adj[node]:
                    if nei not in vis:
                        vis.add(nei)
                        q.append((nei,node))
                    elif nei != parent:
                        return True
        return False