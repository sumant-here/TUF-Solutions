from collections import deque 
class Solution:
    def minimumMultiplications(self, arr, start, end):
        dist = [10**9] * 100000
        q = deque()
        dist[start] = 0 
        q.append((start,0))
        while q :
            num , step = q.popleft()
            if num == end:
                return step
            for x in arr:
                new_n = (num * x) % 100000
                if step + 1 < dist[new_n]:
                    dist[new_n] = step + 1
                    q.append((new_n,step + 1))
        return -1 
     