import heapq
class Solution:
    def MinimumEffort(self, heights):
        m = len(heights)
        n  = len(heights[0])
        dirc = [(-1,0),(0,-1),(1,0),(0,1)]
        dist = [[10**6for _ in range(n)]for _ in range(m)]
        dist[0][0] = 0 
        q= []
        
        heapq.heappush(q,(0,0,0))
        while q:
            eff , r , c  = heapq.heappop(q)
            if r == m-1 and c == n-1:
                return eff
            if eff > dist[r][c]:
                
                continue
            for x , y in dirc:
                nr =  x + r
                nc = y + c
                if 0<= nr < m and 0<= nc < n :
                    curr_eff = abs(heights[nr][nc]- heights[r][c])
                    new_eff = max(curr_eff,eff)
                    if new_eff < dist[nr][nc]:
                        dist[nr][nc] = new_eff
                        heapq.heappush(q,(new_eff,nr,nc))
        return 0 
                    
        
      